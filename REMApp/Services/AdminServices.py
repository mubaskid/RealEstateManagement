from abc import ABCMeta, abstractmethod, ABC
from typing import List, Dict

from django.db.models import Q

from REMApp.Repositories import AdminRepository
from REMApp.Repositories.AdminRepository import CreateAdminDto, UpdateAdminDto, ListAdminDto, DeleteAdminDto, \
    AdminDetailsDto
from REMApp.dto.CommonDto import SelectOptionDto


class AdminManagementService(metaclass=ABCMeta):
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


class DefaultAdminManagementService(AdminManagementService, ABC):
    repository: AdminRepository = None

    def __init__(self, repository: AdminRepository):
        self.repository = repository

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()

    def create(self, model: CreateAdminDto):
        return self.repository.create(model)

    def update(self, id: int, model: UpdateAdminDto):
        return self.repository.update(id, model)

    def list(self) -> List[ListAdminDto]:
        return self.repository.list()

    def delete(self, models: DeleteAdminDto):
        return self.repository.delete()

    def get(self, admin_id: int) -> AdminDetailsDto:
        return self.repository.get(admin_id)
