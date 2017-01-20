from django.contrib import admin
from .models import Question, Hint

admin.site.register(Question)
admin.site.register(Hint)