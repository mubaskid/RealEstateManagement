class CreateAdminDto:
    Admin_id: int
    Username: str
    email: str
    first_name: str
    last_name: str
    password: str
    contact: str
    address: str


class UpdateAdminDto:
    Admin_id: int
    email: str
    first_name: str
    last_name: str
    contact: str


class ListAdminDto:
    email: str
    username: str


class AdminDetailsDto:
    Admin_id: str
    Username: str
    email: str
    first_name: str
    last_name: str
    password: str
    contact: str
    address: str
