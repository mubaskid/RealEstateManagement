from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from REMApp.Services.ServiceFactory import REMApp_service_container
from REMApp.dto.AgentDto import CreateAgentDto, UpdateAgentDto, AgentDetailsDto, ListAgentDto
from REMApp.models import Agent
from django.contrib.auth.decorators import login_required


def create_agent(request):
    context = {

    }
    __create_if_post_method(context, request)
    if request.method == "POST" and context["saved"]:
        return redirect("home_agent")
    return render(request, "Agent/CreateAgent.html", context)


def edit_agent(request, Agent_id):
    agent_details_dto = __get_agent_details_dto_or_raise_404(Agent_id)
    context = {
        "title": f"Edit Agent {agent_details_dto.firstName}",
        "agent": agent_details_dto,
    }
    new_agent_details_dto = __edit_if_post_method(context, Agent_id, request)
    if new_agent_details_dto is not None:
        context["client"] = new_agent_details_dto
    return render(request, "Agent/EditAgent.html", context)


def list_agent(request, Agent_id):
    agent = __get_list_agent_dto_or_raise_404(Agent_id)
    context = {
        "title": f"Agent{agent.Username}",
        "agent": agent
    }
    return render(request, "Agent/", context)


def delete_agent(request, Agent_id: str):
    try:
        Agent().delete(Agent_id, request)
        return redirect("home_agent")
    except Exception:
        raise Http404("Agent does not exist")


def view_agent(request, Agent_id):
    agent = __get_agent_details_dto_or_raise_404(Agent_id)
    context = {
        "title": f"Agent{agent.Agent_id}",
        "agent": agent
    }
    return render(request, "Agent/ViewAgent.html", context)


@login_required(login_url='login')
def home_agent(request):
    agent = REMApp_service_container.agent_management_service().list()
    context = {
        "title": "Agent",
        "agent": agent
    }
    return render(request, "Agent/HomeAgent.html", context)


def get_agent_for_select(request):
    agent = REMApp_service_container.agent_management_service().get_all_for_select_list()
    context = {
        "Agent": agent
    }
    return JsonResponse(context, request)


def __create_if_post_method(context, request):
    if request.method == "POST":
        try:
            agent = __get_create_agent_dto_from_request(request)
            create_agent(request).create(agent)
            context["saved"] = True
        except Exception as c:
            print(c)
            context["saved"] = False


def __edit_if_post_method(context, Agent_id: str, request: HttpRequest) -> AgentDetailsDto:
    if request.method == "POST":
        try:
            client = __get_edit_agent_dto_from_request(Agent_id, request)
            REMApp_service_container.agent_management_service().update(Agent_id, client)
            context["saved"] = True
            return __get_agent_details_dto_or_raise_404(Agent_id)
        except Exception as c:
            print(c)
            context["saved"] = False


def __get_create_agent_dto_from_request(request: HttpRequest) -> CreateAgentDto:
    create_agent_dto = CreateAgentDto()
    create_agent_dto.lastName = request.POST["last_name"]
    __set_agent_attributes_from_request_create(create_agent_dto, request)
    return create_agent_dto


def __get_edit_agent_dto_from_request(Agent_id: str, request: HttpRequest) -> UpdateAgentDto:
    update_agent_dto = UpdateAgentDto()
    update_agent_dto.id = Agent_id
    __set_agent_attributes_from_request_update(update_agent_dto, request)
    return update_agent_dto


def __set_agent_attributes_from_request_update(update_agent_dto, request):
    update_agent_dto.firstName = request.POST["firstName"]
    update_agent_dto.lastName = request.POST["lastName"]
    update_agent_dto.email = request.POST["email"]
    update_agent_dto.Username = request.POST["Username"]
    update_agent_dto.password = request.POST["password"]


def __set_agent_attributes_from_request_create(create_agent_dto, request):
    create_agent_dto.Username = request.POST["username"]
    create_agent_dto.password = request.POST["password"]
    create_agent_dto.firstName = request.POST["firstName"]
    create_agent_dto.lastName = request.POST["lastName"]
    create_agent_dto.email = request.POST["email"]
    create_agent_dto.address = request.POST["address"]
    create_agent_dto.contact = request.POST["contact"]
    create_agent_dto.password = request.POST["password"]


def __get_agent_details_dto_or_raise_404(Agent_id) -> AgentDetailsDto:
    try:
        agent = REMApp_service_container.agent_management_service().get(Agent_id=Agent_id)
    except Agent.DoesNotExist:
        raise Http404("The requested agent does not exist")
    return agent


def __get_list_agent_dto_or_raise_404(Agent_id) -> ListAgentDto:
    try:
        agent = REMApp_service_container.agent_management_service().list(Agent_id)
    except Agent.DoesNotExist:
        raise Http404("List of agents not found")
    return agent
