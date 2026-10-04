from django.shortcuts import render, get_object_or_404
from .models import Question
from django.http import HttpResponse


def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_questions": latest_questions}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = f"You are looking at the response of the question {question_id} lmao."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id} lmao.")
