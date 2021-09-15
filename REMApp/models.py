import uuid

from django.db import models
from django.contrib.auth.models import User


# abstract base user class
class Client(models.Model):
    User = models.OneToOneField(User, on_delete=models.RESTRICT)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to="", width_field=260, height_field=300)
    client_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contact = models.CharField(max_length=14, unique=True)


class Agent(models.Model):
    agent_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    User = models.OneToOneField(User, on_delete=models.RESTRICT)
    contact = models.CharField(max_length=14, unique=True)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to="", width_field=360, height_field=400)


class Admin(models.Model):
    User = models.OneToOneField(User, on_delete=models.RESTRICT)
    contact = models.CharField(max_length=14, unique=True)
    address = models.CharField(max_length=40)

    def __str__(self):
        return f"Full Name: {self.User}"


class Appointment(models.Model):
    appointment_description = models.CharField(max_length=50)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    client_id = models.ForeignKey(Client, on_delete=models.RESTRICT)
    agent_id = models.ManyToManyField(Agent)
    status = [("AP", "Approved"),
              ("PD", "Pending"),
              ("OC", "Occupied")
              ]

    appointmentStatus = models.CharField(max_length=60)
    status = models.CharField(max_length=2, choices=status)
    admin_id = models.ForeignKey(Admin, on_delete=models.RESTRICT)


class Property_category(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=50)
    admin_id = models.ForeignKey(Admin, on_delete=models.RESTRICT)


class Property(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    property_code = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=50, unique=True)
    price = models.FloatField(max_length=150)
    propertyStatus = [("SD", "Sold"),
                      ("FS", "For Sale"),
                      ("OC", "Occupied"),
                      ("TL", "To-Let"),
                      ]
    status = models.CharField(max_length=2, choices=propertyStatus)

    image = models.ImageField(upload_to="REMApp", width_field=360, height_field=400)

    def __str__(self):
        return f"House Name: {self.name}, House Number: {self.property_code}"


class Comment(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.RESTRICT)
    client_id = models.ForeignKey(Client, on_delete=models.RESTRICT)
    comment_time = models.TimeField(auto_now=False, auto_now_add=False)
    comment = models.CharField(max_length=50)
    admin_id = models.ForeignKey(Admin, on_delete=models.RESTRICT)


class Notification(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
