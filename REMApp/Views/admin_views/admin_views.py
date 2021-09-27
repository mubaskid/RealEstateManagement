from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from REMApp.Services.ServiceFactory import REMApp_service_container
from REMApp.dto.AdminDto import CreateAdminDto, UpdateAdminDto, AdminDetailsDto, ListAdminDto
from REMApp.models import Admin
from django.contrib.auth.decorators import login_required


def create_admin(request):
    context = {

    }
    __create_if_post_method(context, request)
    if request.method == "POST" and context["saved"]:
        return redirect("home_admin")
    return render(request, "Admin/CreateAdmin.html", context)


def edit_admin(request, Admin_id):
    admin_details_dto = __get_admin_details_dto_or_raise_404(Admin_id)
    context = {
        "title": f"Edit Admin {admin_details_dto.firstName}",
        "client": admin_details_dto,
    }
    new_admin_details_dto = __edit_if_post_method(context, Admin_id, request)
    if new_admin_details_dto is not None:
        context["admin"] = new_admin_details_dto
    return render(request, "Admin/EditAdmin.html", context)


def list_admin(request, Client_id):
    admin = __get_admin_details_dto_or_raise_404(Client_id)
    context = {
        "title": f"Admin{admin.Username}",
        "admin": admin
    }
    return render(request, "Admin/ViewAdmin.html", context)


def delete_admin(request, Admin_id: str):
    try:
        Admin().delete(Admin_id, request)
        return redirect("home_admin")
    except Exception:
        raise Http404("Admin does not exist")


def view_admin(request, Admin_id: str):
    admin = __get_admin_details_dto_or_raise_404(Admin_id)
    context = {
        "title": f"Admin{admin.Admin_id}",
        "admin": admin
    }
    return render(request, "Admin/ViewAdmin.html", context)


@login_required(login_url='login')
def home_admin(request):
    admin = REMApp_service_container.admin_management_service().list()
    context = {
        "title": "Admin",
        "admin": admin
    }
    return render(request, "Admin/HomeAdmin.html", context)


def get_admin_for_select(request):
    admin = REMApp_service_container.AdminManagementService.get_all_for_select_list()
    context = {
        "admin": admin
    }
    return JsonResponse(context, request)


def __create_if_post_method(context, request):
    if request.method == "POST":
        try:
            admin = __get_create_admin_dto_from_request(request)
            REMApp_service_container.admin_management_service(request).create(admin)
            context["saved"] = True
        except Exception as a:
            print(a)
            context["saved"] = False


def __edit_if_post_method(context, Admin_id: str, request: HttpRequest) -> AdminDetailsDto:
    if request.method == "POST":
        try:
            admin = __get_edit_admin_dto_from_request(Admin_id, request)
            REMApp_service_container.admin_management_service().update(Admin_id, admin)
            context["saved"] = True
            return __get_admin_details_dto_or_raise_404(Admin_id)
        except Exception as c:
            print(c)
            context["saved"] = False


def __get_create_admin_dto_from_request(request: HttpRequest) -> CreateAdminDto:
    create_admin_dto = CreateAdminDto()
    create_admin_dto.lastName = request.POST["last_name"]
    __set_admin_attributes_from_request(create_admin_dto, request)
    return create_admin_dto


def __get_edit_admin_dto_from_request(Admin_id: str, request: HttpRequest) -> UpdateAdminDto:
    update_admin_dto = UpdateAdminDto()
    update_admin_dto.id = Admin_id
    __set_admin_attributes_from_request(update_admin_dto, request)
    return update_admin_dto


def __set_admin_attributes_from_request(update_admin_dto, request):
    update_admin_dto.firstName = request.POST["first_name"]
    update_admin_dto.lastName = request.POST["last_name"]
    update_admin_dto.email = request.POST["email"]
    update_admin_dto.contact = request.POST["contact"]
    update_admin_dto.Username = request.POST["userName"]
    update_admin_dto.password = request.POST["password"]


def __set_admin_attributes_from_request_create(create_admin_dto, request):
    create_admin_dto.userName = request.POST["username"]
    create_admin_dto.password = request.POST["password"]
    create_admin_dto.firstName = request.POST["user_first_name"]
    create_admin_dto.lastName = request.POST["user_last_name"]
    create_admin_dto.email = request.POST["email"]
    create_admin_dto.address = request.POST["address"]
    create_admin_dto.contact = request.POST["contact"]
    create_admin_dto.password = request.POST["password"]


def __get_admin_details_dto_or_raise_404(Admin_id) -> AdminDetailsDto:
    try:
        admin = REMApp_service_container.admin_management_service().get(Admin_id=Admin_id)
    except Admin.DoesNotExist:
        raise Http404("The requested admin does not exist")
    return admin


def __get_list_admin_dto_or_raise_404(email) -> ListAdminDto:
    try:
        admin = REMApp_service_container.admin_management_service().get(email=email)
    except Admin.DoesNotExist:
        raise Http404("List of admins not found")
    return admin
