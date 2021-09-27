from abc import ABCMeta, abstractmethod, ABC
from typing import List
from django.contrib.auth.models import User, Group

from REMApp.dto.AppointmentDto import BookAppointmentDto, ListAppointmentDto, UpdateAppointmentDto, ViewAppointmentDto
from REMApp.dto.CommonDto import SelectOptionDto
from REMApp.models import Appointment


class Appointment_repository(metaclass=ABCMeta):
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
        """views details of an appointment"""
        raise NotImplementedError

    @abstractmethod
    def get(self, client_id: int):
        """gets a single appointment"""
        raise NotImplementedError


class DjangoORMAppointmentRepository(Appointment_repository, ABC):
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        appoint = Appointment.objects.get("Appointment_description", "client_id")
        return [SelectOptionDto(t["client_id"], t["status"]) for t in appoint]

    def book(self, model: BookAppointmentDto):
        point = Appointment()
        point.appointment_description = model.appointment_description
        point.time = model.time

        # Books appointment
        appoint = User.objects.create(model.appointment_description, model.time, model.date, model.agent_id, model.date)
        appoint.client_id = model.client_id
        appoint.admin_id = model.admin_id
        appoint.save()

        point.appoint = appoint
        point = Group.objects.get(user_set__client__appointment="Client")
        point.appoint.add()

        point.save()

    def update(self, model: UpdateAppointmentDto):
        try:
            appointment = Appointment.objects.get(appointment_description="appointment_description")
            appointment.date = model.date
            appointment.time = model.time
            appointment.save()
        except Appointment.DoesNotExist as a:
            message = "Such appointment does not exist"
            print(message)
            raise a

    def view(self, model: ViewAppointmentDto):
        view = list(Appointment.objects.values("appointment_description",
                                               "time",
                                               "date",
                                               "appointmentStatus"))
        results: [ViewAppointmentDto] = []
        for v in view:
            item = ViewAppointmentDto
            item.appointment_description = v["appointment_description"]
            item.time = v["time"]
            item.date = v["date"]
            item.appointmentStatus = v["appointmentStatus"]
        return results

    def list(self) -> List[ListAppointmentDto]:
        des = list(Appointment.objects.values("id"
                                              "appointment_description",
                                              "status",
                                              "time",
                                              "date"))
        result: List[ListAppointmentDto] = []
        for d in des:
            item = ListAppointmentDto()
            item.client_id = d["client_id"]
            item.appointment_description = d["appointment_description"]
            item.appointmentStatus = d["status"]
            item.time = d["time"]
            item.date = d["date"]
        return result
