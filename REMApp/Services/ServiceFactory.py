from dependency_injector import containers, providers

from REMApp.Repositories.ClientRepository import Client_repositories, DjangoORMClientRepository
from REMApp.Repositories.PropertyRepository import Property_repositories, DjangoORMPropertyRepository
from REMApp.Repositories.CommentRepository import Comment_repository, DjangoORMCommentRepository
from REMApp.Repositories.AgentRepository import Agent_repositories, DjangoORMAgentRepository
from REMApp.Repositories.AdminRepository import Admin_repositories, DjangoORMAdminRepository
from REMApp.Repositories.NotificationRepository import Notification_repository, DjangoORMNotificationRepository
from REMApp.Repositories.AppointmentRepository import Appointment_repository, DjangoORMAppointmentRepository
from REMApp.Repositories.PropertyCategoryRepository import PropertyCategoryRepository, \
    DjangoORMPropertyCategoryRepository
from REMApp.Services.AdminServices import AdminManagementService, DefaultAdminManagementService
from REMApp.Services.AgentService import AgentManagementService, DefaultAgentManagementService
from REMApp.Services.ClientService import ClientManagementService, DefaultClientManagementService
from REMApp.Services.AppointmentService import AppointmentManagementService, DefaultAppointmentManagementService
from REMApp.Services.CommentService import CommentManagementService, DefaultCommentManagementService
from REMApp.Services.NotificationService import NotificationManagementService, DefaultNotificationManagementService
from REMApp.Services.PropertyCategoryService import PropertyTypeManagementService, DefaultPropertyTypeManagementService
from REMApp.Services.PropertyService import PropertyManagementService, DefaultPropertyManagementService

from typing import Callable


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    admin_repositories: Callable[[], Admin_repositories] = providers.Factory(
        DjangoORMAdminRepository
    )

    agent_repositories: Callable[[], Agent_repositories] = providers.Factory(
        DjangoORMAgentRepository
    )

    client_repositories: Callable[[], Client_repositories] = providers.Factory(
        DjangoORMClientRepository
    )

    property_repositories: Callable[[], Property_repositories] = providers.Factory(
        DjangoORMPropertyRepository
    )

    comment_repository: Callable[[], Comment_repository] = providers.Factory(
        DjangoORMCommentRepository
    )

    notification_repository: Callable[[], Notification_repository] = providers.Factory(
        DjangoORMNotificationRepository
    )

    property_category_repository: Callable[[], PropertyCategoryRepository] = providers.Factory(
        DjangoORMPropertyCategoryRepository
    )

    appointment_repository: Callable[[], Appointment_repository] = providers.Factory(
        DjangoORMAppointmentRepository
    )

    admin_management_service: Callable[[], AdminManagementService] = providers.Factory(
        DefaultAdminManagementService,
        repository=admin_repositories
    )

    agent_management_service: Callable[[], AgentManagementService] = providers.Factory(
        DefaultAgentManagementService,
        repository=agent_repositories
    )
    client_management_service: Callable[[], ClientManagementService] = providers.Factory(
        DefaultClientManagementService,
        repository=client_repositories
    )

    property_management_service: Callable[[], PropertyManagementService] = providers.Factory(
        DefaultPropertyManagementService,
        repository=property_repositories
    )

    comment_management_service: Callable[[], CommentManagementService] = providers.Factory(
        DefaultCommentManagementService,
        repository=comment_repository
    )

    appointment_management_service: Callable[[], AppointmentManagementService] = providers.Factory(
        DefaultAppointmentManagementService,
        repository=appointment_repository
    )

    property_type_management_service: Callable[[], PropertyTypeManagementService] = providers.Factory(
        DefaultPropertyTypeManagementService,
        repository=property_category_repository
    )

    notification_management_service: Callable[[], NotificationManagementService] = providers.Factory(
        DefaultNotificationManagementService,
        repository=notification_repository
    )


REMApp_service_container = Container()
