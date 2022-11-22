from django.shortcuts import render, redirect
from .models import CoursesData, ContactData, CommentData
from django.http import HttpResponse
from .forms import ContactForm, RegistrationForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def registrationpage(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'registrationpage.html', {'form':form})
    else:
        RegistrationForm(request.POST or None)
        if form.is_valid():
           new_user = form.save(commit=False)
           new_user.set_password(form.request.cleaned_data['password'])
           new_user.save()
           return redirect('loginpage')
        else:
            return HttpResponse('Invalid Data')



def loginpage(request):
    if request.method == 'GET':
        return render(request, 'loginpage.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            messages.success(request, 'Login Successfull')
            return redirect('homepage')
        else:
            return HttpResponse('Invalid User')
def logoutpage(request):
    logout(request)
    messages.success(request, "Logout Successfull")
    return redirect('loginpage')

@login_required(login_url = 'loginpage')
def homepage(request):
    return render(request, 'homepage.html')

@login_required(login_url = 'loginpage')  
def contactpage(request):
    if request.method=='GET':
        form = ContactForm()
        return render(request, 'contactpage.html', {'form':form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactData(
            first_name = request.POST.get('first_name'),
            last_name= request.POST.get('last_name'),
            email = request.POST.get('email'),
            mobile = request.POST.get('mobile'),
            location = request.POST.get('location'),
            courses = request.POST.get('courses'),
            referred_by = request.POST.get('referred_by')
       ).save()
        form = ContactForm()
        return render(request, 'contactpage.html', {'form':form})


@login_required(login_url = 'loginpage')
def servicespage(request):
    courses = CoursesData.objects.all()
    return render(request, 'servicespage.html', {'courses': courses})

@login_required(login_url = 'loginpage')
def feedbackpage(request):
    comments = CommentData.objects.all().order_by('-id')
    if request.method == "GET":
        form = CommentForm()
        return render(request, 'feedbackpage.html', {'form': form, 'comments':comments})
    else:
        form = CommentForm(request.POST or None)
        if form.is_valid():
           content = request.POST.get('content')
           user = request.user

           data = CommentData.objects.create(user=user, content=content)
           data.save()
           return render(request, 'feedbackpage.html', {'form': form, 'comments': comments})

@login_required(login_url = 'loginpage')
def gallerypage(request):
    return render(request, 'gallerypage.html')


