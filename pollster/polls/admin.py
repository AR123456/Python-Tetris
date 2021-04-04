from django.contrib import admin

# Register your models here.
from.models import Question, Choice

#customize the site header
admin.site.site_header = "Would You Rather Admin"
admin.site.site_title = "Would You Rather Admin Area"
admin.site.index_title = "Welcome to the Would You Rather admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question,QuestionAdmin)