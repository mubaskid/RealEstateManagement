from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from REMApp.Services.ServiceFactory import REMApp_service_container
from REMApp.dto.PropertyCategoryDto import CreatePropertyCategoryDto, UpdatePropertyCategoryDto, \
    ListPropertyCategoryDto, PropertyCategoryDetailsDto
from REMApp.models import Property_category
from django.contrib.auth.decorators import login_required


def create_property_category(request):
    context = {

    }
    __create_if_post_method(context, request)
    if request.method == "POST" and context["saved"]:
        return redirect("home_property_category")
    return render(request, "", context)


def edit_property_category(request, property_category_id):
    property_category_details_dto = __get_property_details_dto_or_raise_404(property_category_id)
    context = {
        "title": f"Edit property {property_category_details_dto.description}",
        "property": property_category_details_dto,
    }
    new_property_category_details_dto = __edit_if_post_method(context, property_category_id, request)
    if new_property_category_details_dto is not None:
        context["property"] = new_property_category_details_dto
    return render(request, "", context)


def list_property(request, property_category_id):
    property_category = __get_property_details_dto_or_raise_404(property_category_id)
    context = {
        "title": f"Property{property_category.description}",
        "property_category": property_category
    }
    return render(request, "", context)


def delete_property(request, property_category_id: int):
    try:
        Property_category().delete(property_category_id, request)
        return redirect("home_property")
    except Exception:
        raise Http404("Property does not exist")


def view_property(request, property_category_id: int):
    properties = __get_property_details_dto_or_raise_404(property_category_id)
    context = {
        "title": f"PropertyCategory{properties.property_category_id}",
        "properties": properties
    }
    return render(request, "", context)


@login_required(login_url='login')
def home_property_category(request):
    properties = REMApp_service_container.property_type_management_service().list()
    context = {
        "title": "PropertyCategory",
        "properties": properties
    }
    return render(request, "", context)


def get_property_category_for_select(request):
    property_category = REMApp_service_container.property_type_management_service().get_all_for_select_list()
    context = {
        "property_category": property_category
    }
    return JsonResponse(context, request)


def __create_if_post_method(context, request):
    if request.method == "POST":
        try:
            property_category = __get_create_property_dto_from_request(request)
            REMApp_service_container.property_type_management_service(request).create(property_category)
            context["saved"] = True
        except Exception as a:
            print(a)
            context["saved"] = False


def __edit_if_post_method(context, property_category_id: int, request: HttpRequest) -> PropertyCategoryDetailsDto:
    if request.method == "POST":
        try:
            properties = __get_edit_property_category_dto_from_request(property_category_id, request)
            REMApp_service_container.property_type_management_service().update(property_category_id, properties)
            context["saved"] = True
            return __get_property_details_dto_or_raise_404(property_category_id)
        except Exception as p:
            print(p)
            context["saved"] = False


def __get_create_property_dto_from_request(request: HttpRequest) -> CreatePropertyCategoryDto:
    create_property_category_dto = CreatePropertyCategoryDto()
    create_property_category_dto.name = request.POST["name_name"]
    create_property_category_dto.property_category_id = request.POST["property_category_id"]
    create_property_category_dto.description = request.POST["description"]
    __set_property_category_attributes_from_request(create_property_category_dto, request)
    return create_property_category_dto


def __get_edit_property_category_dto_from_request(property_category_id: int, request: HttpRequest) -> \
        UpdatePropertyCategoryDto:
    update_property_category_dto = UpdatePropertyCategoryDto()
    update_property_category_dto.id = property_category_id
    __set_property_category_attributes_from_request(update_property_category_dto, request)
    return update_property_category_dto


def __set_property_category_attributes_from_request(update_property_category_dto, request):
    update_property_category_dto.name = request.POST["name"]
    update_property_category_dto.property_category_id = request.POST["property_category_id"]


def __get_property_details_dto_or_raise_404(property_category_id) -> PropertyCategoryDetailsDto:
    try:
        properties = REMApp_service_container.property_type_management_service().get(id=property_category_id)
    except Property_category.DoesNotExist:
        raise Http404("The requested admin does not exist")
    return properties


def __get_list_property_dto_or_raise_404(property_id) -> ListPropertyCategoryDto:
    try:
        properties = REMApp_service_container.property_management_service().get(id=property_id)
    except Property_category.DoesNotExist:
        raise Http404("List of Properties not found")
    return properties
