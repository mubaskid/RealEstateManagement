from abc import ABCMeta, abstractmethod, ABC
from typing import List

# from django.db.models import Q

from REMApp.Repositories import PropertyCategoryRepository
from REMApp.dto.CommonDto import SelectOptionDto
from REMApp.dto.PropertyCategoryDto import CreatePropertyCategoryDto, \
    UpdatePropertyCategoryDto, ListPropertyCategoryDto, FindPropertyCategoryDto


class PropertyCategoryManagementService(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Selects an option"""
        raise NotImplementedError

    @abstractmethod
    def create(self, models: CreatePropertyCategoryDto):
        """Creates a property type"""
        raise NotImplementedError

    @abstractmethod
    def update(self, models: UpdatePropertyCategoryDto):
        """Updates a property Type"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListPropertyCategoryDto]:
        """Lists the Property Types"""
        raise NotImplementedError

    @abstractmethod
    def find(self, filter: str) -> List[FindPropertyCategoryDto]:
        """Finds a property type"""
        raise NotImplementedError


class DefaultPropertyCategoryManagementService(PropertyCategoryManagementService, ABC):
    repository: PropertyCategoryRepository = None

    def __init__(self, repository: PropertyCategoryRepository):
        self.repository = repository

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()

    def create(self, models: CreatePropertyCategoryDto):
        return self.repository.create()

    def update(self, models: UpdatePropertyCategoryDto):
        return self.repository.update()

    def list(self) -> List[ListPropertyCategoryDto]:
        return self.repository.list()

    def find(self, filter: str) -> List[FindPropertyCategoryDto]:
        return self.repository.find()
