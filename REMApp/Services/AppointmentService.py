from abc import ABCMeta, abstractmethod, ABC
from typing import List  # Dict#

# from django.db.models import Q#

from REMApp.Repositories import AppointmentRepository
from REMApp.dto.CommonDto import SelectOptionDto
from REMApp.dto.AppointmentDto import BookAppointmentDto, ListAppointmentDto, UpdateAppointmentDto, ViewAppointmentDto


class AppointmentManagementService(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Selects an option"""
        raise NotImplementedError

    @abstractmethod
    def book(self, model: BookAppointmentDto):
        """Books an appointment"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListAppointmentDto]:
        """Lists appointments"""
        raise NotImplementedError

    @abstractmethod
    def update(self, model: UpdateAppointmentDto):
        """updates Appointments"""
        raise NotImplementedError

    def view(self, model: ViewAppointmentDto):
        """views Appointment details"""
        raise NotImplementedError

    @abstractmethod
    def get(self, Client_id: str):
        """gets a single appointment"""
        raise NotImplementedError


class DefaultAppointmentManagementService(AppointmentManagementService, ABC):
    repository: AppointmentRepository = None

    def __init__(self, repository: AppointmentRepository):
        self.repository = repository

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()

    def book(self, model: BookAppointmentDto):
        return self.repository.book()

    def list(self) -> List[ListAppointmentDto]:
        return self.repository.list()

    def update(self, model: UpdateAppointmentDto):
        return self.repository.update()

    def get(self, Client_id: int):
        return self.repository.get()
