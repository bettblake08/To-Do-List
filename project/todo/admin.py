# todo/admin
from django.contrib import admin
# local models
from .models import Todo

admin.site.register(Todo)
