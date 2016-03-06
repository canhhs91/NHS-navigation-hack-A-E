from django.contrib import admin

# Register your models here.


from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'next_if_yes', 'next_if_no')


admin.site.register(Question, QuestionAdmin)
