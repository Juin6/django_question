from django.shortcuts import render, redirect
from .models import Question, Comment, Reply
from .forms import QuestionForm
import random

# Create your views here.
def index(request):
    questions = Question.objects.all()

    context = {
        'questions':questions,
    }

    return render(request, 'index.html', context)

def detail(request,id):
    question = Question.objects.get(id=id)
    count_A = question.comment_set.filter(answer='A').count()
    count_B = question.comment_set.filter(answer='B').count()

    if count_A==0 and count_B == 0:
        context = {
            'question':question,
        }

    else:
        percent_A = count_A / (count_A + count_B) * 100
        percent_B = count_B / (count_A + count_B) * 100 
        # comment = Comment.objects.filter(id=comment.id)

        context = {
            'question': question,
            'percent_A': percent_A,
            'percent_B': percent_B,
            #  'comment':comment,
        }
        
    return render(request, 'detail.html', context)

def create(request):

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('choose:index')

    else:
        form = QuestionForm()

    context = {
        'form':form,
    }

    return render(request, 'create.html', context)

def delete(request, id):
    question = Question.objects.get(id=id)
    question.delete()

    return redirect('choose:index')


def comment_create(request,id):
    comment = Comment()
    comment.answer = request.GET.get('answer')
    comment.comment = request.GET.get('comment')
    comment.question_id = id
    comment.save()

    return redirect('choose:detail', id=id)

def comment_delete(request, comment_id, id):
    question = Question.objects.get(id=id)
    comment = question.comment_set.filter(id=comment_id)
    comment.delete()

    return redirect('choose:detail', id=id)


def myRandom(request):
    number = Question.objects.all().count()
    id = random.choice(range(1,number+1))

    return redirect('choose:detail', id=id)

def reply(request, question_id, id):
    reply = Reply() 
    reply.reply = request.GET.get('reply')
    reply.comment_id = id
    reply.save()
    return redirect('choose:detail',id=question_id)