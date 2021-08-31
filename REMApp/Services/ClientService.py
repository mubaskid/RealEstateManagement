from abc import ABCMeta, abstractmethod
from typing import List, Dict

from django.db.models import Q

from REMApp.dto.CommonDto import SelectOptionDto
from REMApp.dto.Client_dto import CreateClientDto, UpdateClientDto, ListClientDto, DeleteClientDto, FindClientDto, ClientDetailsDto


class ClientRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """View Options"""
        raise NotImplementedError

    @abstractmethod
    def create(self, models: CreateClientDto):
        """Create Client"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListClientDto]:
        """Gets list of Clients"""
        raise NotImplementedError

    @abstractmethod
    def update(self, client_id: int, model: UpdateClientDto):
        """Updates Clients details"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, models: DeleteClientDto):
        """Deletes Client"""
        raise NotImplementedError

    @abstractmethod
    def find(self, models: FindClientDto):
        """Looks for a particular Client"""
        raise NotImplementedError

    @abstractmethod
    def get(self, client_id: int):
        """Gets clients details"""
        raise NotImplementedError
