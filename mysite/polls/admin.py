from django.contrib import admin
from .models import Question

# add django admin site support
admin.site.register(Question)
