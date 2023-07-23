from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Answer, Like


from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def front_page(request):
    # questions = Question.objects.all().order_by('-created_at')[:10]  # Display the latest 10 questions
    # return render(request, 'front_page.html', {'questions': questions})
    questions = Question.objects.filter(is_approved=True).order_by('-created_at')[:10]
    answers = Answer.objects.filter(is_approved=True)
    return render(request, 'front_page.html', {'questions': questions, 'answers': answers})

@login_required
def post_question(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Question.objects.create(title=title, content=content, author=request.user)
        return redirect('home')  # Use the name 'home' to redirect to the homepage
    return render(request, 'post_question.html')

@login_required
def view_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'view_question.html', {'question': question, 'answers': answers})

@login_required
def post_answer(request, question_id):
    if request.method == 'POST':
        content = request.POST['content']
        question = Question.objects.get(pk=question_id)
        Answer.objects.create(content=content, question=question, author=request.user)
        return redirect('view_question', question_id=question_id)
    return render(request, 'post_answer.html', {'question_id': question_id})

@login_required
def like_answer(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    Like.objects.create(user=request.user, answer=answer)
    return redirect('view_question', question_id=answer.question.id)

