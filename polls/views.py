from http.client import HTTPResponse

from django.shortcuts import render

# Create your views here.

def index(request):
    return HTTPResponse("Hello World")



def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request,
                  )

def vote(request):
    choice_id = request.POST["choice"]
    choice = Choice.objects.get(id=choice_id)
    choice.votes +=1
    choice.save()
    return redirect("detail",question_id=choice.question.id)