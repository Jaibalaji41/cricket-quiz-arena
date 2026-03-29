from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Question, Attempt, Leaderboard

admin.site.register(User, UserAdmin)
admin.site.register(Question)
admin.site.register(Attempt)
admin.site.register(Leaderboard)
