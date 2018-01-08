from django.contrib import admin
from .models import Question, Choice

# add django admin site support
admin.site.register(Question)
admin.site.register(Choice)