from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import UserTask

admin.site.register(UserTask, SimpleHistoryAdmin)

