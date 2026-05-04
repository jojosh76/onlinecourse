from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# 1. ChoiceInline : Pour ajouter des choix directement dans une Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

# 2. QuestionInline : Pour ajouter des questions directement dans une Leçon
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2

# 3. QuestionAdmin : Configuré avec ChoiceInline
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# 4. LessonAdmin : Configuré avec QuestionInline
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]

# 5. CourseAdmin (Optionnel mais recommandé si non présent)
class CourseAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# Enregistrement des modèles
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Submission)