from django.contrib import admin

from .models import Choice, Question
from django.utils import timezone
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    inlines = [ChoiceInline]
    search_fields = ["question_text"]
 
admin.site.register(Question, QuestionAdmin)
