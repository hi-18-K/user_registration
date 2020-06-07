from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm  #bcoz we are uing UserRegisterForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

#views inside users:-

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!')
            #return redirect('/todoapp/') #name of todoapp homepage
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


def index(request):
    #context = {
    #    'posts': Post.objects.all()
    #}
    #if request.method == "POST": #checking if the request method is a POST
    return render(request, 'users/index.html')
