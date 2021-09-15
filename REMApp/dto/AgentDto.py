class CreateAgentDto:
    Username: str
    password: str
    email: str
    User_first_name: str
    User_last_name: str
    address: str
    contact: str
    Agent_id: str


class UpdateAgentDto:
    Username: str
    email: str
    address: str


class ListAgentDto:
    id: int
    Username: str


class AgentDetailsDto:
    Username: str
    password: str
    email: str
    User_first_name: str
    User_last_name: str
    address: str
    contact: str
    id: int
