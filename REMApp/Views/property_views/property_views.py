from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from REMApp.Services.ServiceFactory import REMApp_service_container
from REMApp.dto.PropertyDto import CreatePropertyDto, UpdatePropertyDto, PropertyDetailsDto, ListPropertyDto
from REMApp.models import Property
# from django.contrib.auth.decorators import login_required


def create_property(request):
    context = {

    }
    __create_if_post_method(context, request)
    if request.method == "POST" and context["saved"]:
        return redirect("home_property")
    return render(request, "", context)


def edit_property(request, property_code):
    property_details_dto = __get_property_details_dto_or_raise_404(property_code)
    context = {
        "title": f"Edit property {property_details_dto.name}",
        "property": property_details_dto,
    }
    new_property_details_dto = __edit_if_post_method(context, property_code, request)
    if new_property_details_dto is not None:
        context["property"] = new_property_details_dto
    return render(request, "", context)


def list_property(request, property_code):
    properties = __get_property_details_dto_or_raise_404(property_code)
    context = {
        "title": f"Property{properties.name}",
        "properties": properties
    }
    return render(request, "", context)


def delete_property(request, property_code: str):
    try:
        Property().delete(property_code, request)
        return redirect("home_property")
    except Exception:
        raise Http404("Property does not exist")


def view_property(request, property_code: str):
    properties = __get_property_details_dto_or_raise_404(property_code)
    context = {
        "title": f"Property{properties.property_code}",
        "properties": properties
    }
    return render(request, "", context)


# @login_required(login_url='login')
def home_property(request):
    properties = REMApp_service_container.property_management_service().list()
    context = {
        "title": "Property",
        "properties": properties
    }
    return render(request, "", context)


def get_property_for_select(request):
    properties = REMApp_service_container.property_management_service().get_all_for_select_list()
    context = {
        "property": properties
    }
    return JsonResponse(context, request)


def __create_if_post_method(context, request):
    if request.method == "POST":
        try:
            admin = __get_create_property_dto_from_request(request)
            REMApp_service_container.property_management_service(request).create(admin)
            context["saved"] = True
        except Exception as a:
            print(a)
            context["saved"] = False


def __edit_if_post_method(context, property_code: str, request: HttpRequest) -> PropertyDetailsDto:
    if request.method == "POST":
        try:
            properties = __get_edit_property_dto_from_request(property_code, request)
            REMApp_service_container.property_management_service().update(property_code, properties)
            context["saved"] = True
            return __get_property_details_dto_or_raise_404(property_code)
        except Exception as p:
            print(p)
            context["saved"] = False


def __get_create_property_dto_from_request(request: HttpRequest) -> CreatePropertyDto:
    create_property_dto = CreatePropertyDto()
    create_property_dto.lastName = request.POST["last_name"]
    __set_property_attributes_from_request(create_property_dto, request)
    return create_property_dto


def __get_edit_property_dto_from_request(property_code: str, request: HttpRequest) -> UpdatePropertyDto:
    update_property_dto = UpdatePropertyDto()
    update_property_dto.id = property_code
    __set_property_attributes_from_request(update_property_dto, request)
    return update_property_dto


def __set_property_attributes_from_request(update_property_dto, request):
    update_property_dto.name = request.POST["name"]
    update_property_dto.property_code = request.POST["property_code"]
    update_property_dto.price = request.POST["price"]
    update_property_dto.description = request.POST["description"]
    update_property_dto.propertyStatus = request.POST["status"]
    update_property_dto.image = request.POST["image"]


def __set_property_attributes_from_request_create(create_property_dto, request):
    create_property_dto.name = request.POST["name"]
    create_property_dto.property_code = request.POST["property_code"]
    create_property_dto.description = request.POST["description"]
    create_property_dto.id = request.POST["id"]
    create_property_dto.price = request.POST["price"]
    create_property_dto.propertyStatus = request.POST["propertyStatus"]
    create_property_dto.address = request.POST["address"]
    create_property_dto.image = request.POST["image"]


def __get_property_details_dto_or_raise_404(Property_code) -> PropertyDetailsDto:
    try:
        properties = REMApp_service_container.property_management_service().get(Property_code=Property_code)
    except Property.DoesNotExist:
        raise Http404("The requested property does not exist")
    return properties


def __get_list_property_dto_or_raise_404(Property_code) -> ListPropertyDto:
    try:
        properties = REMApp_service_container.property_management_service().get(Property_code=Property_code)
    except Property.DoesNotExist:
        raise Http404("List of Properties not found")
    return properties
