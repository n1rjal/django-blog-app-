from django.shortcuts import render , HttpResponse , redirect
# from .froms import voting
from .models import Question , Choice
from django.views.generic import ListView
from django.db.models import F
class view_qestion(ListView):
    model = Question
    template_name = 'index.html'

def vote_here(request , pk_second):
    question = Question.objects.get(pk = pk_second)
    choices = question.choice_set.all()
    context = {'choices' : choices, 'question': question}

    if request.method == 'POST':
        vote = int(request.POST.get('abcd'))
        print(vote)
        choices = Choice.objects.filter(pk=vote).update(votes=F('votes') + 1)
        

    return render(request , 'vote.html', context)
def handel_404(request, exception):
    return render(request,'handel_404.html', status=404  )

def new_vote(request):
    # form = voting()
    if request.method == 'POST':
        question = request.POST.get('question')
        print(question)
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        all_options = (option1 , option2 , option3)
        que_boj = Question(question_text = question)
        que_boj.save()
        choice1 = Choice(choice_text=option1 , question=que_boj)
        choice2 = Choice(choice_text=option2 , question=que_boj)
        choice3 = Choice(choice_text=option3 , question=que_boj)
        choice1.save()
        choice2.save()
        choice3.save()
        print(question , all_options)
    return render(request, 'create_vote.html')

