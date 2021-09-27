from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from REMApp.Services.ServiceFactory import REMApp_service_container
from REMApp.dto.ClientDto import CreateClientDto, UpdateClientDto, ClientDetailsDto, ListClientDto
from REMApp.models import Client
from django.contrib.auth.decorators import login_required


def create_client(request):
    context = {

    }
    __create_if_post_method(context, request)
    if request.method == "POST" and context["saved"]:
        return redirect("home_client")
    return render(request, "Client/CreateClient.html", context)


def edit_client(request, Client_id):
    client_details_dto = __get_client_details_dto_or_raise_404(Client_id)
    context = {
        "title": f"Edit Client {client_details_dto.first_name}",
        "client": client_details_dto,
    }
    new_client_details_dto = __edit_if_post_method(context, Client_id, request)
    if new_client_details_dto is not None:
        context["client"] = new_client_details_dto
    return render(request, "Client/EditClient.html", context)


def list_client(request, Client_id):
    client = __get_list_client_dto_or_raise_404(Client_id)
    context = {
        "title": f"Client{client.userName}",
        "client": client
    }
    return render(request, "Client/ViewClient.html", context)


# def delete_client(request, Client_id: str):
#     try:
#         REMApp_service_container().delete(Client_id, request)
#         return redirect("home_client")
#     except Exception:
#         raise Http404("Client does not exist")


def view_client(request, Client_id):
    client = __get_client_details_dto_or_raise_404(Client_id)
    context = {
        "title": f"Client{client.Client_id}",
        "client": client
    }
    return render(request, "Client/ViewClient.html", context)


@login_required(login_url='login')
def home_client(request):
    client = REMApp_service_container.client_management_service().list()
    context = {
        "title": "Client",
        "client": client
    }
    return render(request, "Client/HomeClient.html", context)


def get_client_for_select(request):
    client = REMApp_service_container.ClientManagementService.get_all_for_select_list()
    context = {
        "client": client
    }
    return JsonResponse(context, request)


def __create_if_post_method(context, request):
    if request.method == "POST":
        try:
            client = __get_create_client_dto_from_request(request)
            REMApp_service_container.client_management_service(request).create(client)
            context["saved"] = True
        except Exception as c:
            print(c)
            context["saved"] = False


def __edit_if_post_method(context, Client_id: str, request: HttpRequest) -> ClientDetailsDto:
    if request.method == "POST":
        try:
            client = __get_edit_client_dto_from_request(Client_id, request)
            REMApp_service_container.client_management_service().edit(Client_id, client)
            context["saved"] = True
            return __get_client_details_dto_or_raise_404(Client_id)
        except Exception as c:
            print(c)
            context["saved"] = False


def __get_create_client_dto_from_request(request: HttpRequest) -> CreateClientDto:
    create_client_dto = CreateClientDto()
    create_client_dto.lastName = request.POST["last_name"]
    __set_client_attributes_from_request(create_client_dto, request)
    return create_client_dto


def __get_edit_client_dto_from_request(Client_id: str, request: HttpRequest) -> UpdateClientDto:
    update_client_dto = UpdateClientDto()
    update_client_dto.id = Client_id
    __set_client_attributes_from_request(update_client_dto, request)
    return update_client_dto


def __set_client_attributes_from_request(update_client_dto, request):
    update_client_dto.firstName = request.POST["first_name"]
    update_client_dto.lastName = request.POST["last_name"]
    update_client_dto.email = request.POST["email"]
    update_client_dto.contact = request.POST["contact"]
    update_client_dto.userName = request.POST["userName"]
    update_client_dto.password = request.POST["password"]


def __set_client_attributes_from_request_create(create_client_dto, request):
    create_client_dto.userName = request.POST["username"]
    create_client_dto.password = request.POST["password"]
    create_client_dto.firstName = request.POST["user_first_name"]
    create_client_dto.lastName = request.POST["user_last_name"]
    create_client_dto.email = request.POST["email"]
    create_client_dto.address = request.POST["address"]
    create_client_dto.contact = request.POST["contact"]
    create_client_dto.password = request.POST["password"]


def __get_client_details_dto_or_raise_404(Client_id) -> ClientDetailsDto:
    try:
        client = REMApp_service_container.client_management_service().get(id=Client_id)
    except Client.DoesNotExist:
        raise Http404("The requested client does not exist")
    return client


def __get_list_client_dto_or_raise_404(Client_id) -> ListClientDto:
    try:
        client = REMApp_service_container.client_management_service().get(id=Client_id)
    except Client.DoesNotExist:
        raise Http404("No Clients found")
    return client
