from django.urls import path

from REMApp.Views.agent_views import agent_views

urlpatterns = [
    path("create", agent_views.create_agent, name="CreateAgent")
]
