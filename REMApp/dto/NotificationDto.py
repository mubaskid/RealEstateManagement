class CreateNotificationDto:
    name: str
    description: str
    time: str


class ListNotificationsDto:
    name: str


class GetNotificationDto:
    name: str
    description: str
    time: str