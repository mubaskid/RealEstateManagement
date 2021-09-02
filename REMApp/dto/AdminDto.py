class CreateAdminDto:
    id: int
    Username: str
    email: str
    User_first_name: str
    User_last_name: str
    password: str
    contact: str
    address: str


class UpdateAdminDto:
    id: int
    email: str
    User_first_name: str
    User_last_name: str
    contact: str


class DeleteAdminDto:
    Username: str
    id: int
    contact: str


class ListAdminDto:
    email: str
    username: str


class AdminDetailsDto:
    id: str
    Username: str
    email: str
    User_first_name: str
    User_last_name: str
    password: str
    contact: str
    address: str
