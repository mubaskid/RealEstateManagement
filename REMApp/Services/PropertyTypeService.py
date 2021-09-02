from abc import ABCMeta, abstractmethod, ABC
from typing import List

from django.db.models import Q

from REMApp.Repositories import PropertyTypeRepository
from REMApp.dto.CommonDto import SelectOptionDto
from REMApp.dto.PropertyTypeDto import CreatePropertyTypeDto, DeletePropertyTypeDto, \
    UpdatePropertyTypeDto, ListPropertyTypeDto, FindPropertyTypeDto


class PropertyTypeManagementService(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Selects an option"""
        raise NotImplementedError

    @abstractmethod
    def create(self, models: CreatePropertyTypeDto):
        """Creates a property type"""
        raise NotImplementedError

    @abstractmethod
    def update(self, models: UpdatePropertyTypeDto):
        """Updates a property Type"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListPropertyTypeDto]:
        """Lists the Property Types"""
        raise NotImplementedError

    @abstractmethod
    def find(self, filter: str) -> List[FindPropertyTypeDto]:
        """Finds a property type"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, models: DeletePropertyTypeDto):
        """Deletes a property type"""
        raise NotImplementedError


class DefaultPropertyTypeManagementService(PropertyTypeManagementService, ABC):
    repository: PropertyTypeRepository = None

    def __init__(self, repository: PropertyTypeRepository):
        self.repository = repository

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()

    def create(self, models: CreatePropertyTypeDto):
        return self.repository.create()

    def update(self, models: UpdatePropertyTypeDto):
        return self.repository.update()

    def list(self) -> List[ListPropertyTypeDto]:
        return self.repository.list()

    def find(self, filter: str) -> List[FindPropertyTypeDto]:
        return self.repository.find()

    def delete(self, models: DeletePropertyTypeDto):
        return self.repository.delete()
