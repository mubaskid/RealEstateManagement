class CreateClientDto:
    Client_id: str
    userName: str
    firstName: str
    lastName: str
    password: str
    email: str
    address: str
    contact: str
    image: str


class UpdateClientDto:
    userName: str
    email: str
    password: str
    contact: str
    firstName: str
    lastName: str


class ListClientDto:
    Client_id: str
    userName: str


class ClientDetailsDto:
    Client_id: str
    userName: str
    first_name: str
    last_name: str
    password: str
    email: str
    address: str
    contact: str
    image: str
