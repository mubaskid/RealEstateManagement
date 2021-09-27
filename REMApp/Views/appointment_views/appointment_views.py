from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from REMApp.Services.ServiceFactory import REMApp_service_container
from REMApp.dto.AppointmentDto import BookAppointmentDto, UpdateAppointmentDto, ListAppointmentDto, ViewAppointmentDto
from REMApp.models import Appointment


# from django.contrib.auth.decorators import login_required


def book_appointment(request):
    context = {

    }
    __book_if_post_method(context, request)
    if request.method == "POST" and context["saved"]:
        return redirect("")
    return render(request, "", context)


def edit_appointment(request, appointment_description):
    appointment_details_dto = __get_view_appointment_dto_or_raise_404(appointment_description)
    context = {
        "title": f"Edit Appointment {appointment_details_dto.appointment_description}",
        "appointment": appointment_details_dto,
    }
    new_appointment_details_dto = __edit_if_post_method(context, appointment_description, request)
    if new_appointment_details_dto is not None:
        context["appointment"] = new_appointment_details_dto
    return render(request, "", context)


def list_appointment(request, date):
    appointment = __get_list_appointment_dto_or_raise_404(date)
    context = {
        "title": f"Appointment{appointment.appointment_description}",
        "agent": appointment
    }
    return render(request, "", context)


def view_appointment(request, appointment_description):
    appoint = __get_view_appointment_dto_or_raise_404(appointment_description)
    context = {
        "title": f"Appointment{appoint.appointment_description}",
        "appoint": appoint
    }
    return render(request, "", context)


# @login_required(login_url='login')
# def home_agent(request):
#     agent = REMApp_service_container.agent_management_service().list()
#     context = {
#         "title": "Agent",
#         "agent": agent
#     }
#     return render(request, "Agent/HomeAgent.html", context)


def get_appointment_for_select(request):
    appoint = REMApp_service_container.appointment_management_service().get_all_for_select_list()
    context = {
        "Appoint": appoint
    }
    return HttpResponse(context, request)


def __book_if_post_method(context, request):
    if request.method == "POST":
        try:
            appoint = __get_book_appointment_dto_from_request(request)
            book_appointment(request).book(appoint)
            context["saved"] = True
        except Exception as c:
            print(c)
            context["saved"] = False


def __edit_if_post_method(context, appointment_description: str, request: HttpRequest) -> ViewAppointmentDto:
    if request.method == "POST":
        try:
            appointment = __get_update_appointment_dto_from_request(appointment_description, request)
            REMApp_service_container.appointment_management_service().update(appointment_description, appointment)
            context["saved"] = True
            return __get_view_appointment_dto_or_raise_404(appointment_description)
        except Exception as c:
            print(c)
            context["saved"] = False


def __get_book_appointment_dto_from_request(request: HttpRequest) -> BookAppointmentDto:
    book_appointment_dto = BookAppointmentDto()
    book_appointment_dto.appointment_description = request.POST["appointment_description"]
    __set_appointment_attributes_from_request_book(book_appointment_dto, request)
    return book_appointment_dto


def __get_update_appointment_dto_from_request(appointment_description: str, request: HttpRequest) -> \
        UpdateAppointmentDto:
    update_appointment_dto = UpdateAppointmentDto()
    update_appointment_dto.id = appointment_description
    __set_appointment_attributes_from_request_update(update_appointment_dto, request)
    return update_appointment_dto


def __set_appointment_attributes_from_request_update(update_appointment_dto, request):
    update_appointment_dto.appointment_description = request.POST["appointment_description"]
    update_appointment_dto.date = request.POST["date"]
    update_appointment_dto.time = request.POST["time"]


def __set_appointment_attributes_from_request_book(book_appointment_dto, request):
    book_appointment_dto.appointment_description = request.POST["appointment_description"]
    book_appointment_dto.date = request.POST["date"]
    book_appointment_dto.time = request.POST["time"]
    book_appointment_dto.Admin_id = request.POST["Admin_id"]
    book_appointment_dto.Client_id = request.POST["Client_id"]
    book_appointment_dto.Agent_id = request.POST["Agent_id"]
    book_appointment_dto.appointmentStatus = request.POST["appointStatus"]


def __get_view_appointment_dto_or_raise_404(appointment_description) -> ViewAppointmentDto:
    try:
        appoint = REMApp_service_container.appointment_management_service().get(
            appointment_description=appointment_description)
    except Appointment.DoesNotExist:
        raise Http404("Such appointment does not exist")
    return appoint


def __get_list_appointment_dto_or_raise_404(appointment_description) -> ListAppointmentDto:
    try:
        appoint = REMApp_service_container.appointment_management_service().list(appointment_description)
    except Appointment.DoesNotExist:
        raise Http404("List of appointments not found")
    return appoint
