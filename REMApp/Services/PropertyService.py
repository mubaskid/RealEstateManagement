from abc import ABCMeta, abstractmethod, ABC
from typing import List

from django.db.models import Q

from REMApp.Repositories import PropertyRepository
from REMApp.dto.CommonDto import SelectOptionDto
from REMApp.dto.PropertyDto import CreatePropertyDto, UpdatePropertyDto, FindPropertyDto, ListPropertyDto, \
    DeletePropertyDto, PropertyDetailsDto


class PropertyManagementService(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Create an order object"""
        raise NotImplementedError

    @abstractmethod
    def create(self, model: CreatePropertyDto):
        """Create Property object"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, property_id: int, model: UpdatePropertyDto):
        """Update Property object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListPropertyDto]:
        """Gets list of Property"""
        raise NotImplementedError

    @abstractmethod
    def details(self, property_id: int, model: PropertyDetailsDto):
        """Return Property Details"""
        raise NotImplementedError

    @abstractmethod
    def find(self, property_id: int, model: FindPropertyDto):
        """Searches for a property"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, property_id: int, model: DeletePropertyDto):
        """"Deletes Property Details"""
        raise NotImplementedError

    @abstractmethod
    def get(self, property_id: int):
        """Gets a single Property"""
        raise NotImplementedError


class DefaultPropertyManagementService(PropertyManagementService, ABC):
    repository: PropertyRepository = None

    def __init__(self, repository: PropertyRepository):
        self.repository = repository

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()

    def create(self, model: CreatePropertyDto):
        return self.repository.create()

    def edit(self, property_id: int, model: UpdatePropertyDto):
        return self.repository.create()

    def list(self) -> List[ListPropertyDto]:
        return self.repository.list()

    def delete(self, property_id: int, model: DeletePropertyDto):
        return self.repository.edit()

    def details(self, property_id: int, model: PropertyDetailsDto):
        return self.repository.details()
