from django.contrib import admin
from .models import Voter

# this will register Voter to the admin interface
admin.site.register(Voter)
