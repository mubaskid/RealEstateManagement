from abc import ABCMeta, abstractmethod, ABC
from typing import List
from django.contrib.auth.models import Group

from REMApp.dto.PropertyDto import CreatePropertyDto, UpdatePropertyDto, ListPropertyDto, PropertyDetailsDto
from REMApp.dto.CommonDto import SelectOptionDto
from REMApp.models import Property


class Property_repositories(metaclass=ABCMeta):
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
    def delete(self, property_id: int):
        """"Deletes Property Details"""
        raise NotImplementedError

    @abstractmethod
    def get(self, property_id: int):
        """Gets a single Property"""
        raise NotImplementedError


class DjangoORMPropertyRepository(Property_repositories, ABC):
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        properties = Property.objects.values("id", "property_code", "propertyStatus")
        return [SelectOptionDto(p["id"], p["description"]) for p in properties]

    def create(self, model: CreatePropertyDto):
        properties = Property()
        properties.name = model.name
        properties.property_code = model.property_code
        properties.description = model.description
        properties.id = model.id
        properties.propertyStatus = model.propertyStatus
        properties.price = model.price
        properties.image = model.image

        # create the user
        properties = Property.objects.create(model.name, model.property_code, model.description, model.id,
                                             model.propertyStatus, model.price, model.image)
        properties.name = model.name
        properties.property_code = model.property_code
        properties.description = model.description
        properties.id = model.id
        properties.propertyStatus = model.propertyStatus
        properties.price = model.price
        properties.image = model.image
        properties.save()

        properties.user = property
        properties = Group.objects.get(name='Property')
        properties.groups.add(property)

        properties.save()

    def edit(self, property_id: int, model: UpdatePropertyDto):
        try:
            properties = Property.objects.get(id=property_id)
            properties.name = model.name
            properties.property_code = model.property_code
            properties.propertyStatus = model.propertyStatus
            properties.save()
        except Property.DoesNotExist as p:
            message = "Property does not exist"
            print(message)
            raise p

    def list(self) -> List[ListPropertyDto]:
        admin = list(Property.objects.values("name",
                                             "property_code"
                                             ))
        result: List[ListPropertyDto] = []
        for p in admin:
            item = ListPropertyDto()
            item.name = p["name"]
            item.property_code = p["property_code"]
            result.append(item)
        return result

    def get(self, property_id: int):
        try:
            properties = Property.objects.get(id=property_id)
            result = PropertyDetailsDto()
            result.id = properties.id

            result.name = properties.name
            result.property_code = properties.property_code
            return properties
        except Property.DoesNotExist as p:
            message = "client does not exist"
            print(message)
            raise p
