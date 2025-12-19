from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from .forms import Create_po, Create_mo
from .models import Post, Cm
from django.contrib.auth.forms import UserCreationForm

def home(request):
    # Получаем все посты из базы данных
    posts = Post.objects.all()
    return render(request, 'main/home.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = Create_po(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Create_po()
    return render(request,'main/create_post.html',
                  {'form': form})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    # Перенаправление после успешной регистрации
    template_name = 'registration/signup.html'

def create_category(request):
    if request.method == 'POST':
        form = Create_mo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Create_mo()
    return render(request,'main/create_category.html',
                  {'form': form})



def post_detail(request,pk): #primari key - первичный ключ/уникальный номер
    post = get_object_or_404(Post, pk=pk)
    return render(request,'main/post.html',
                  {'post': post})
