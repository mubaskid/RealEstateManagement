from abc import ABCMeta, abstractmethod, ABC
from typing import List  # Dict#

# from django.db.models import Q#

from REMApp.Repositories import ClientRepository
from REMApp.dto.CommonDto import SelectOptionDto
from REMApp.dto.ClientDto import CreateClientDto, UpdateClientDto, ListClientDto, ClientDetailsDto


class ClientManagementService(metaclass=ABCMeta):
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
    def update(self, Client_id: int, model: UpdateClientDto):
        """Updates Clients details"""
        raise NotImplementedError

    @abstractmethod
    def get(self, Client_id: int):
        """Gets clients details"""
        raise NotImplementedError


class DefaultClientManagementService(ClientManagementService, ABC):
    repository: ClientRepository = None

    def __init__(self, repository: ClientRepository):
        self.repository = repository

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()

    def create(self, model: CreateClientDto):
        return self.repository.create(model)

    def update(self, Client_id: int, model: UpdateClientDto):
        return self.repository.update(id, model)

    def list(self) -> List[ListClientDto]:
        return self.repository.list()

    def get(self, Client_id: int) -> ClientDetailsDto:
        return self.repository.get(Client_id)
