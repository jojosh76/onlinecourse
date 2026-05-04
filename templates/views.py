from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Choice, Submission, Lesson

def submit(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == 'POST':
        # Logique de soumission + calcul score
        submission = Submission.objects.create(user=request.user, lesson=lesson)
        score = 0
        total = 0
        for question in lesson.question_set.all():
            selected = request.POST.get(f'question_{question.id}')
            if selected:
                choice = Choice.objects.get(pk=selected)
                if choice.is_correct:
                    score += 1
            total += 1
        # Enregistrer score...
        return redirect('show_exam_result', submission_id=submission.id)
    return render(request, 'exam.html', {'lesson': lesson})

def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    if submission.user != request.user:
        return redirect('home')
    # Calcul résultats détaillés
    context = {
        'submission': submission,
        'score': ...,  # ton calcul
        'total': ...,
        'percentage': ...,
    }
    return render(request, 'result.html', context)