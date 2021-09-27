from django.urls import path

from REMApp.Views.client_views import client_views

urlpatterns = [
    path("create", client_views.create_client, name="CreateClient"),
    path("delete<str:Client_id>", client_views.delete_client, name="DeleteClient"),
    path("edit/<str:Client_id>", client_views.edit_client, name="EditClient"),
    path("list/<str:Client_id>", client_views.list_client, name="ListClient"),
    path("view/<str:Client_id>", client_views.view_client, name="ViewClient"),
    path("home", client_views.home_client, name="HomeClient"),
]
