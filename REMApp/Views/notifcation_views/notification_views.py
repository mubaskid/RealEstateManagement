from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from REMApp.Services.ServiceFactory import REMApp_service_container
from REMApp.dto.NotificationDto import *
from REMApp.models import Notification


def create_notification(request):
    context = {

    }
    __create_if_post_method(context, request)
    if request.method == "POST" and context["saved"]:
        return redirect("")
    return render(request, "", context)


def list_notification(request, name):
    notify = __get_list_notification_dto_or_raise_404(name)
    context = {
        "title": f"Notification{notify.name}",
        "notify": notify
    }
    return render(request, "", context)


def get_notification(request):
    notify = REMApp_service_container.notification_management_service().get_all_for_select_list()
    context = {
        "Notification": notify
    }
    return HttpResponse(context, request)


def __create_if_post_method(context, request):
    if request.method == "POST":
        try:
            notify = __get_create_notification_dto_from_request(request)
            create_notification(request).create(notify)
            context["saved"] = True
        except Exception as c:
            print(c)
            context["saved"] = False


def __get_create_notification_dto_from_request(request: HttpRequest) -> CreateNotificationDto:
    create_notification_dto = CreateNotificationDto()
    create_notification_dto.appointment_description = request.POST["description"]
    __set_notification_attributes_from_request_create(create_notification_dto, request)
    return create_notification_dto


def __set_notification_attributes_from_request_create(create_notification_dto, request):
    create_notification_dto.name = request.POST["name"]
    create_notification_dto.description = request.POST["description"]
    create_notification_dto.time = request.POST["time"]


def __get_list_notification_dto_or_raise_404(description) -> ListNotificationsDto:
    try:
        notify = REMApp_service_container.notification_management_service().list(description)
    except Notification.DoesNotExist:
        raise Http404("You have no Notifications")
    return notify


def __get_notification_dto_or_raise_404(description) -> GetNotificationDto:
    try:
        notify = REMApp_service_container.notification_management_service().get(
            appointment_description=description)
    except Notification.DoesNotExist:
        raise Http404("Notification does not exist")
    return notify
