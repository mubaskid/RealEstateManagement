class CreateAdminDto:
    Admin_id: int
    Username: str
    email: str
    firstName: str
    lastName: str
    password: str
    contact: str
    address: str


class UpdateAdminDto:
    Admin_id: int
    email: str
    firstName: str
    lastName: str
    contact: str
    Username: str
    password: str


class ListAdminDto:
    email: str
    Username: str


class AdminDetailsDto:
    Admin_id: str
    Username: str
    email: str
    firstName: str
    lastName: str
    password: str
    contact: str
    address: str
