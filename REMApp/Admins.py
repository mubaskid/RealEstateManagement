from django.contrib import admin

# Register your models here.
from REMApp.models import *

admin.site.register(Admin)
admin.site.register(Client)
admin.site.register(Agent)
admin.site.register(Property)
admin.site.register(Property_type)
admin.site.register(Property_image)
admin.site.register(Appointment)
admin.site.register(Notification)
admin.site.register(Comment)
