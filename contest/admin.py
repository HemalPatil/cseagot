from django.contrib import admin
from .models import Question, Hint, Solve

admin.site.register(Question)
admin.site.register(Hint)
admin.site.register(Solve)