from django.urls import path

from REMApp.Views.admin_views import admin_views

urlpatterns = [
    path("create", admin_views.create_admin, name="CreateAdmin")
]
