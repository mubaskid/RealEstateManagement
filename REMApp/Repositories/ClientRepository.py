from abc import ABCMeta, abstractmethod, ABC
from typing import List

from django.contrib.auth.models import User, Group
from REMApp.dto.ClientDto import CreateClientDto, UpdateClientDto, ListClientDto, ClientDetailsDto
from REMApp.dto.CommonDto import SelectOptionDto
from REMApp.models import Client


class Client_repositories(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """View Options"""
        raise NotImplementedError

    @abstractmethod
    def create(self, models: CreateClientDto):
        """Create Client"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListClientDto]:
        """Gets list of Clients"""
        raise NotImplementedError

    @abstractmethod
    def update(self, Client_id: str, model: UpdateClientDto):
        """Updates Clients details"""
        raise NotImplementedError

    @abstractmethod
    def get(self, Client_id: str):
        """Gets clients details"""
        raise NotImplementedError


class DjangoORMClientRepository(Client_repositories, ABC):
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        client = Client.User.email("id", "user__last_name")
        return [SelectOptionDto(i["id"], i["last_name"]) for i in client]

    def create(self, model: CreateClientDto):
        client = Client()
        client.address = model.address
        client.contact = model.contact

        # create the user
        user = User.objects.get(model.userName, model.email, model.password)
        user.user_first_name = model.firstName
        user.user_last_name = model.lastName
        user.save()

        client.user = user
        client = Group.objects.get(name='Admin')
        user.groups.add(client)

        client.save()

    def update(self, Client_id: str, model: UpdateClientDto):
        try:
            client = Client.objects.values(id=Client_id)
            client.Username = model.userName
            client.User_last_name = model.password
            client.email = model.email
            client.contact = model.contact
            client.save()
        except Client.DoesNotExist as i:
            message = "Client does not exist"
            print(message)
            raise i

    def list(self) -> List[ListClientDto]:
        admin = list(Client.objects.values("id",
                                           "user__first_name",
                                           "user__last_name",
                                           "user__email",
                                           "address",
                                           "contact"))
        result: List[ListClientDto] = []
        for i in admin:
            item = ListClientDto()
            item.id = i["id"]
            item.user_first_name = i["user__first_name"]
            item.user_last_name = i["user__last_name"]
            item.user_email = i["user__email"]
            item.address = i["address"]
            item.contact = i["contact"]
            result.append(item)
        return result

    def get(self, Client_id: str):
        try:
            client = Client.objects.get(id=Client_id)
            result = ClientDetailsDto()
            result.id = client.id
            result.user_first_name = client.user.first_name
            result.user_last_name = client.user.last_name
            result.user_email = client.User.email
            result.address = client.address
            result.contact = client.contact
            return client
        except Client.DoesNotExist as c:
            message = "Client does not exist"
            print(message)
            raise c
