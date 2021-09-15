class BookAppointmentDto:
    appointment_description: str
    date: str
    time: str
    client_id: int
    admin_id: int
    agent_id: int


class ListAppointmentDto:
    appointment_description: str
    status: str
    time: None
    date: None
    client_id: int


class UpdateAppointmentDto:
    appointment_description: str
    date: str
    time: str



