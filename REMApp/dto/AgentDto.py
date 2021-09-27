class CreateAgentDto:
    Username: str
    password: str
    email: str
    firstName: str
    lastName: str
    address: str
    contact: str
    Agent_id: str


class UpdateAgentDto:
    Username: str
    email: str
    address: str
    firstName: str
    lastName: str
    password: str


class ListAgentDto:
    Agent_id: str
    Username: str


class AgentDetailsDto:
    Username: str
    password: str
    email: str
    firstName: str
    lastName: str
    address: str
    contact: str
    Agent_id: str
