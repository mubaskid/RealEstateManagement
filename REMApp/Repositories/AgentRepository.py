from abc import ABCMeta, abstractmethod, ABC
from typing import List

from django.contrib.auth.models import User, Group
from REMApp.dto.AgentDto import CreateAgentDto, UpdateAgentDto, ListAgentDto, AgentDetailsDto
from REMApp.dto.CommonDto import SelectOptionDto
from REMApp.models import Agent


class Agent_repositories(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Create Agent"""
        raise NotImplementedError

    @abstractmethod
    def create(self, model: CreateAgentDto):
        """Create Admin"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, Agent_id: str, model: UpdateAgentDto):
        """Update agent object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListAgentDto]:
        """Gets list of Agents"""
        raise NotImplementedError

    @abstractmethod
    def details(self, Agent_id: str) -> AgentDetailsDto:
        """Return Agent Details"""
        raise NotImplementedError

    @abstractmethod
    def get(self, Agent_id: str):
        """Gets a single Agent"""
        raise NotImplementedError


class DjangoORMAgentRepository(Agent_repositories, ABC):
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        admin = Agent.User.email("id", "user__last_name")
        return [SelectOptionDto(a["id"], a["last_name"]) for a in admin]

    def create(self, model: CreateAgentDto):
        agent = Agent()
        agent.address = model.address
        agent.contact = model.contact

        # create the user
        user = User.objects.create_user(model.Username, model.email, model.password)
        User.user_first_name = model.firstName
        User.user_last_name = model.lastName
        User.save(user)

        Agent.User = User
        agent = Group.objects.get(name='Agent')
        User.groups.add(agent)

        agent.save()

    def edit(self, Agent_id: str, model: UpdateAgentDto):
        try:
            agent = Agent.User.email(id=Agent_id)
            agent.Username = model.Username
            agent.email = model.email
            agent.address = model.address
            agent.save()
        except Agent.DoesNotExist as c:
            message = "Agent does not exist"
            print(message)
            raise c

    def list(self) -> List[ListAgentDto]:
        agent = list(Agent.User.email("id",
                                      "user__first_name",
                                      "user__last_name",
                                      "user__email",
                                      "address",
                                      "contact"))
        result: List[ListAgentDto] = []
        for a in agent:
            agent = ListAgentDto()
            result.id = a["id"]
            result.Username = a["username"]
            result.append(agent)
        return result

    def get(self, Agent_id: str):
        try:
            agent = Agent.objects.get(id=Agent_id)
            result = AgentDetailsDto()
            result.id = agent.id

            result.user_first_name = agent.user.first_name
            result.user_last_name = agent.user.last_name
            result.user_email = agent.User.email
            result.address = agent.address
            result.contact = agent.contact
            return agent

        except Agent.DoesNotExist as a:
            message = "Agent does not exist"
            print(message)
            raise a
