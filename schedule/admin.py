from django.contrib import admin
from .models import Route, Stop, Schedule

admin.site.register(Route)
admin.site.register(Stop)
admin.site.register(Schedule)