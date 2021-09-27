class BookAppointmentDto:
    appointment_description: str
    date: str
    time: str
    Client_id: str
    Admin_id: int
    Agent_id: str
    appointmentStatus: str


class ListAppointmentDto:
    appointment_description: str
    status: str
    time: None
    date: None
    Client_id: int
    appointmentStatus: str


class UpdateAppointmentDto:
    appointment_description: str
    date: str
    time: str


class ViewAppointmentDto:
    appointment_description: str
    date: str
    time: str
    appointmentStatus: str
