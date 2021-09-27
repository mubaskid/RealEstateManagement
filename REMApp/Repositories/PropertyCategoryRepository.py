from abc import ABCMeta, abstractmethod
from typing import List
from django.contrib.auth.models import User, Group
from django.db.models import Q

from REMApp.dto.PropertyCategoryDto import CreatePropertyCategoryDto, ListPropertyCategoryDto, \
    PropertyCategoryDetailsDto, UpdatePropertyCategoryDto
from REMApp.dto.CommonDto import SelectOptionDto
from REMApp.models import Property_category


class PropertyCategoryRepository(metaclass=ABCMeta):
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
    def find(self, filter: str) -> List[PropertyCategoryDetailsDto]:
        """Finds a property type"""
        raise NotImplementedError


class DjangoORMPropertyCategoryRepository(PropertyCategoryRepository, ABCMeta):
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        listType = Property_category.objects.get("name", "description")
        return [SelectOptionDto(e["id"], e["name"]) for e in listType]

    def create(self, models: CreatePropertyCategoryDto):
        createT = Property_category()
        createT.name = models.name
        createT.description = models.description

        #
        created = User.objects.get(property_category="description")
        created.propertyTypeid = models.property_category_id
        created.name = models.name
        created.save()

        createT.created = created
        createT = Group.objects.get(property_category="name")
        createT.created.add()

        createT.save()

    def list(self) -> List[ListPropertyCategoryDto]:
        listThis = list(Property_category.objects.values("id",
                                                         "description"))
        result: List[ListPropertyCategoryDto] = []
        for t in listThis:
            item = ListPropertyCategoryDto()
            item.id = t["id"]
            item.description = t["description"]
            return result

    def update(self, models: UpdatePropertyCategoryDto):
        try:
            item = Property_category.objects.get(id=id)
            item.name = models.name
            item.id = models.property_category_id
            item.save()
        except Property_category.DoesNotExist as a:
            message = "Property type does not exist"
            print(message)
            raise a

    def find(self, filter: str) -> List[PropertyCategoryDetailsDto]:
        property_type = Property_category.objects
        if filter is not None:
            property_type = property_type.filter(Q(item_name__contains=filter) | Q(item_description__contains=filter))

        property_type = list(property_type)
        result = []
        for p in property_type:
            result = PropertyCategoryDetailsDto()
            result.description = p.description
        return result
