from abc import ABCMeta, abstractmethod, ABC
from typing import List  # Dict#
# from django.db.models import Q

from REMApp.Repositories import AgentRepository
from REMApp.dto.CommonDto import SelectOptionDto
from REMApp.dto.AgentDto import CreateAgentDto, UpdateAgentDto, ListAgentDto, AgentDetailsDto


class AgentManagementService(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """View Options"""
        raise NotImplementedError

    @abstractmethod
    def create(self, models: CreateAgentDto):
        """Create Client"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListAgentDto]:
        """Gets list of Clients"""
        raise NotImplementedError

    @abstractmethod
    def update(self, client_id: int, model: UpdateAgentDto):
        """Updates Clients details"""
        raise NotImplementedError

    def details(self, models: AgentDetailsDto):
        """Gets Agent Details"""
        raise NotImplementedError

    @abstractmethod
    def get(self, client_id: int):
        """Gets clients details"""
        raise NotImplementedError


class DefaultAgentManagementService(AgentManagementService, ABC):
    repository: AgentRepository = None

    def __init__(self, repository: AgentRepository):
        self.repository = repository

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()

    def create(self, model: CreateAgentDto):
        return self.repository.create(model)

    def update(self, Agent_id: int, model: UpdateAgentDto):
        return self.repository.update(Agent_id, model)

    def list(self) -> List[ListAgentDto]:
        return self.repository.list()

    def get(self, Agent_id: int) -> AgentDetailsDto:
        return self.repository.get(Agent_id)
