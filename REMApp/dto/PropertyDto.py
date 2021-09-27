class CreatePropertyDto:
    name: str
    property_code: str
    description: str
    id: int
    price: float
    propertyStatus: str
    address: str
    image: str


class UpdatePropertyDto:
    name: str
    property_code: str
    price: float
    description: str
    address: str
    propertyStatus: str
    image: str


class ListPropertyDto:
    name: str
    property_code: str


class PropertyDetailsDto:
    name: str
    property_code: str
    description: str
    id: int
    price: float
    propertyStatus: str
    address: str
