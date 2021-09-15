class CreatePropertyTypeDto:
    name: str
    description: str
    propertyTypeid: int


class UpdatePropertyTypeDto:
    name: str
    propertyTypeid: int


class ListPropertyTypeDto:
    propertyTypeid: int
    description: str


class FindPropertyTypeDto:
    propertyTypeid: int
    description: str
