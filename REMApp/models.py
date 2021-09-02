from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    User = models.OneToOneField(User, on_delete=models.RESTRICT)
    address = models.CharField(max_length=50)
    image = models.ImageField(name="Avatar", width_field=260, height_field=300)
    id = models.IntegerField(max_length=11)
    contact = models.CharField(max_length=250)


class Agent(models.Model):
    agent_id = models.IntegerField(max_length=11)
    User = models.OneToOneField(User, on_delete=models.RESTRICT)
    contact = models.CharField(max_length=14, unique=True)
    address = models.CharField(max_length=50)
    image = models.ImageField(name="Avatar", width_field=360, height_field=400)


class Appointment(models.Model):
    appointment_description = models.CharField(max_length=250)
    date = models.DateField()
    time = models.TimeField()
    client_id = models.ForeignKey(Client, on_delete=models.RESTRICT)
    agent_id = models.ManyToManyField(Agent)
    status = models.BooleanField()
    admin_id = models.ForeignKey(Agent, on_delete=models.RESTRICT)


class Admin(models.Model):
    User = models.OneToOneField(User, on_delete=models.RESTRICT)
    contact = models.CharField(max_length=14, unique=True)
    address = models.CharField(max_length=40)

    def __str__(self):
        return f"Full Name: {self.User}"


class Property_type(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=50)
    admin_id = models.ForeignKey(Admin, on_delete=models.RESTRICT)


class Property_image(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=50)
    property_id = models.IntegerField(max_length=11)


class Property(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    property_number = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=50, unique=True)
    price = models.FloatField(max_length=150)
    image = models.ImageField(name="Avatar", width_field=360, height_field=400)

    def __str__(self):
        return f"House Name: {self.name}, House Number: {self.property_number}"


class Comment(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.RESTRICT)
    client_id = models.ForeignKey(Client, on_delete=models.RESTRICT)
    comment_time = models.DateTimeField
    date = models.DateField
    status = models.CharField(max_length=50)
    admin_id = models.ForeignKey(Admin, on_delete=models.RESTRICT)


class Notification(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
