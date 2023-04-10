from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import models
from . import backend
from . import database

# Create your views here.
def index(request):
    return redirect('bugs')


def signup(request):
    if request.method == "POST":
        database.insert_user('a', 'a', 'a', 'a', 'a')

    return render(request, 'sign-up.html')
    # if request.user.is_authenticated:
    #     return redirect('index')
    
    # if request.method == "POST":
    #     email_address = request.POST['email']
    #     username = request.POST['username']

    #     first_name = request.POST['firstname']
    #     last_name = request.POST['lastname']

    #     password = request.POST['password']
    #     confirm_password = request.POST['confirm-password']

    #     email_valid = backend.validate_email(email_address)

    #     if not email_valid:
    #         messages.info(request, 'Email address is not valid!')
    #         return redirect('signup')

    #     username_valid = backend.validate_username(username)

    #     if not username_valid:
    #         messages.info(request, 'Username is not valid!')
    #         return redirect('signup')

    #     password_valid = backend.validate_password(password)

    #     # Regex used:
    #     # Minimum 8 letters, at least one capitalized letter, at least one lowercase letter, at least one digit
    #     if not password_valid:
    #         messages.info(request, 'Your password is too weak!')
    #         return redirect('signup')

    #     if password != confirm_password:
    #         messages.info(request, "Passwords don't match!")
    #         return redirect('signup')

    #     if first_name == "":
    #         messages.info(request, "The first name cannot be left blank!")
    #         return redirect('signup')

    #     if last_name == "":
    #         messages.info(request, "The last name cannot be left blank!")
    #         return redirect('signup')

    #     # Check if email exists
    #     if User.objects.filter(email=email_address).exists():
    #         messages.info(request, 'Email is already taken!')
    #         return redirect('signup')

    #     # Check if the username exists
    #     elif User.objects.filter(username=username).exists():
    #         messages.info(request, 'Username is already taken!')
    #         return redirect('signup')

    #     # At this point, all the user data should be valid!

    #     new_user = User.objects.create_user(username=username, email=email_address, password=password,
    #                                         first_name=first_name, last_name=last_name)
    #     new_user.save()

    #     auth.authenticate(username=username, password=password)

    #     new_collab = models.Collaborator(user=new_user)
    #     new_collab.save()

    #     # Change this to signin once implemented
    #     return redirect('index')

    # else:
    #     return render(request, 'sign-up.html')

def signin(request):
        return render(request, 'sign-in.html')

def assign_leader(request):
        return render(request, 'assign-leader.html')

def assign_user(request):
        return render(request, 'assign-user.html')

def assign_team(request):
        return render(request, 'assign-team.html')

def bugs(request):
        return render(request, 'bugs.html')

def features(request):
        return render(request, 'features.html')

def create_bug(request):
    if request.method == "POST":
        project = request.POST['project-select']
        print("reached")
        print(project)
        print(type(project))
        title = request.POST['title']
        description = request.POST['description']
        date = timezone.now().strftime("%Y-%m-%d")
        database.add_bug(date, title, description, project, 'b')
    database.getProjects()
    con = {"con": database.getProjects()}
    return render(request, 'create-bug.html', con)

def create_feature(request):
    if request.method == "POST":
        project = request.POST['project-select']
        title = request.POST['title']
        description = request.POST['description']
        date = timezone.now().strftime("%Y-%m-%d")
        database.add_featureRequest(date, title, description, project, 'b')
    database.getProjects()
    con = {"con": database.getProjects()}
    return render(request, 'create-feature.html',con)

def create_project(request):
    if request.method == "POST":
        description = request.POST['description']
        status = "Incomplete"
        date = timezone.now().strftime("%Y-%m-%d")
        database.create_project(date, status, description, 'b')
    return render(request, 'create-project.html')

def create_report(request):
    if request.method == "POST":
        ticket = request.POST['ticket-select']
        contents = request.POST['contents']
        date = timezone.now().strftime("%Y-%m-%d")
        database.create_report(ticket, contents, date)
    return render(request, 'create-report.html')

def tickets(request):
        return render(request, 'tickets.html')

def reports(request):
        return render(request, 'reports.html')

def projects(request):
        return render(request, 'projects.html')

def teams(request):
        return render(request, 'teams.html')