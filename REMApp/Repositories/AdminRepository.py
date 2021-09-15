from abc import ABCMeta, abstractmethod, ABC
from typing import List
from django.contrib.auth.models import User, Group

from REMApp.dto.AdminDto import CreateAdminDto, UpdateAdminDto, ListAdminDto, AdminDetailsDto
from REMApp.dto.CommonDto import SelectOptionDto
from REMApp.models import Admin


class Admin_repositories(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Create an order object"""
        raise NotImplementedError

    @abstractmethod
    def create(self, model: CreateAdminDto):
        """Create Admin object"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, Admin_id: int, model: UpdateAdminDto):
        """Update Admin object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListAdminDto]:
        """Gets list of Admins"""
        raise NotImplementedError

    @abstractmethod
    def details(self, admin_id: int) -> AdminDetailsDto:
        """Return Admin Details"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, admin_id: int):
        """"Deletes Admin Details"""
        raise NotImplementedError

    @abstractmethod
    def get(self, admin_id: int):
        """Gets a single Admin"""
        raise NotImplementedError


class DjangoORMAdminRepository(Admin_repositories, ABC):
    #     def get_all_for_select_list(self) -> List[SelectOptionDto]:
    #         admin = Admin.User.email("id", "user__last_name")
    #         return [SelectOptionDto(i["id"], i["last_name"]) for i in admin]

    def create(self, model: CreateAdminDto):
        admin = Admin()
        admin.address = model.address
        admin.contact = model.contact

        # create the user
        user = User.objects.create(model.Username, model.email, model.password)
        user.first_name = model.first_name
        user.last_name = model.last_name
        user.save()

        admin.user = user
        admin = Group.objects.get(name='Admin')
        user.groups.add(admin)

        admin.save()

    def edit(self, admin_id: int, model: UpdateAdminDto):
        try:
            admin = Admin.objects.get(id=admin_id)
            admin.first_name = model.first_name
            admin.last_name = model.last_name
            admin.email = model.email
            admin.contact = model.contact
            admin.save()
        except Admin.DoesNotExist as a:
            message = "Admin does not exist"
            print(message)
            raise a

    def list(self) -> List[ListAdminDto]:
        admin = list(Admin.objects.values("id",
                                          "user__first_name",
                                          "user__last_name",
                                          "user__email",
                                          "address",
                                          "contact"))
        result: List[ListAdminDto] = []
        for a in admin:
            item = ListAdminDto()
            item.admin_id = a["id"]
            item.user_first_name = a["user__first_name"]
            item.user_last_name = a["user__last_name"]
            item.user_email = a["user__email"]
            item.address = a["address"]
            item.contact = a["contact"]
            result.append(item)
        return result

    def get(self, admin_id: int):
        try:
            admin = Admin.objects.get(id=admin_id)
            result = AdminDetailsDto()
            result.id = admin.admin_id

            result.first_name = admin.first_name
            result.last_name = admin.last_name
            result.email = admin.email
            result.address = admin.address
            result.contact = admin.contact
            return admin
        except Admin.DoesNotExist as a:
            message = "Admin does not exist"
            print(message)
            raise a
