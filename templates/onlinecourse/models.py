from django.db import models
from django.conf import settings
from django.utils.timezone import now

# Assurez-vous que vos modèles Course, Lesson et Enrollment existent déjà au-dessus

class Question(models.Model):
    # Relation Many-To-One avec le cours (ou Lesson selon votre structure de lab)
    # Le lab suggère souvent une relation directe avec Course, mais Lesson fonctionne aussi
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    grade = models.IntegerField(default=1)

    # Méthode pour calculer si l'apprenant obtient les points
    def is_get_score(self, selected_ids):
        all_answers = self.choice_set.filter(is_correct=True).count()
        selected_correct = self.choice_set.filter(is_correct=True, id__in=selected_ids).count()
        if all_answers == selected_correct:
            return True
        else:
            return False

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

class Submission(models.Model):
    # Relation avec l'inscription (Enrollment) qui lie l'utilisateur au cours
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE)
    # Relation Many-to-Many avec les choix sélectionnés
    choices = models.ManyToManyField(Choice)
    date_submitted = models.DateTimeField(default=now)