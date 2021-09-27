from abc import ABCMeta, abstractmethod, ABC
from typing import List
from django.contrib.auth.models import User, Group

from REMApp.dto.NotificationDto import CreateNotificationDto, ListNotificationsDto
from REMApp.dto.CommonDto import SelectOptionDto
from REMApp.models import Notification


class Notification_repository(metaclass=ABCMeta):
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


class DjangoORMNotificationRepository(Notification_repository, ABC):
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        notify = Notification.objects.get("name", "description")
        return [SelectOptionDto(n["name"], n["description"]) for n in notify]

    def create(self, model: CreateNotificationDto):
        notify = Notification()
        notify.description = model.description
        notify.name = model.name

        # creates notification
        notice = User.objects.create(model.name, model.description)
        notice.name = model.name
        notice.save()

        notify.notice = notify
        notify = Group.objects.get(user_set="name")
        notify.notice.save()

        notify.save()

    def list(self) -> List[ListNotificationsDto]:
        note = list(Notification.objects.values("description"
                                                ))
        result: List[ListNotificationsDto] = []
        for n in note:
            item = ListNotificationsDto()
            item.description = n["description"]
        return result
