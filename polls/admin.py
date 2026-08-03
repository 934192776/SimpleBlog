
from django.contrib import admin

from polls.models import Question, Choice

# Register your models he
admin.site.register(Question)
admin.site.register(Choice)
