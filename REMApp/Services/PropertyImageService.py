from abc import ABCMeta, abstractmethod, ABC
from typing import List, Dict

from django.db.models import Q

from REMApp.Repositories import PropertyImageRepository
from REMApp.dto.CommonDto import SelectOptionDto
from REMApp.dto.PropertyImageDto import ViewPropertyImage, DeletePropertyImage


class PropertyImageManagementService(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Selects an option"""
        raise NotImplementedError

    @abstractmethod
    def view(self, models: ViewPropertyImage):
        """Views the image of a property"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, model: DeletePropertyImage):
        """Deletes property image"""
        raise NotImplementedError

    @abstractmethod
    def get(self, property_id: int):
        """gets the image of a property"""
        raise NotImplementedError


class DefaultPropertyImageManagementService(PropertyImageManagementService, ABC):
    repository: PropertyImageRepository

    def __int__(self, repository: PropertyImageRepository):
        self.repository = repository

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()

    def view(self, models: ViewPropertyImage):
        return self.repository.view()

    def delete(self, model: DeletePropertyImage):
        return self.repository.delete()

    def get(self, property_id: int):
        return self.repository.get()
