class CreatePropertyCategoryDto:
    name: str
    description: str
    property_category_id: int


class UpdatePropertyCategoryDto:
    name: str
    property_category_id: int


class ListPropertyCategoryDto:
    property_category_id: int
    description: str


class PropertyCategoryDetailsDto:
    property_category_id: int
    description: str
