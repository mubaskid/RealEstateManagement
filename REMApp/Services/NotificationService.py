from abc import ABCMeta, abstractmethod, ABC
from typing import List

# from django.db.models import Q#

from REMApp.Repositories import NotificationRepository
from REMApp.dto.CommonDto import SelectOptionDto
from REMApp.dto.NotificationDto import CreateNotificationDto, ListNotificationsDto


class NotificationManagementService(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Selects an option"""
        raise NotImplementedError

    @abstractmethod
    def create(self, model: CreateNotificationDto):
        """Creates Notification"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListNotificationsDto]:
        """Lists all notification"""
        raise NotImplementedError


class DefaultNotificationManagementService(NotificationManagementService, ABC):
    repository: NotificationRepository = None

    def __init__(self, repository: NotificationRepository):
        self.repository = repository

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()

    def create(self, model: CreateNotificationDto):
        return self.repository.create()

    def list(self) -> List[ListNotificationsDto]:
        return self.repository.list()
