from django.shortcuts import render
from .models import Question
from django.http import HttpResponse

def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_questions": latest_questions}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    return HttpResponse(f"You are looking at question {question_id} lmao.")


def results(request, question_id):
    response = f"You are looking at the response of the question {question_id} lmao."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id} lmao.")
