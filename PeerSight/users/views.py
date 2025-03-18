from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    if request.user.is_authenticated:
        if request.user.role == 'professor':
            return redirect('staff_dashboard')
        elif request.user.role == 'student':
            return redirect('student_dashboard')
        else:
            # If no role is set, show the signin page with a message
            return render(request, "users/signin.html", {'no_role_message': True})
    return render(request, "users/signin.html")

# function receives a request
def logout_view(request):
    logout(request) #logout the user
    return redirect("/") #return the empty route

def is_professor(user):
    return user.is_authenticated and user.role == 'professor'

def is_student(user):
    return user.is_authenticated and user.role == 'student'

@login_required
@user_passes_test(is_professor)
def staff_dashboard(request):
    # Example data - you would typically get this from your database
    context = {
        'username': request.user.username or request.user.email,
        'classes': [
            {
                'code': 'CSCI3356.01',
                'name': 'Software Engineering',
                'term': 'Spring 2025',
                'students': 38,
                'reviews_completed': 29,
                'total_reviews': 38
            },
            {
                'code': 'CSCI3356.02',
                'name': 'Software Engineering',
                'term': 'Spring 2025',
                'students': 31,
                'reviews_completed': 25,
                'total_reviews': 31
            },
            {
                'code': 'CSCI1102.01',
                'name': 'Computer Science I',
                'term': 'Fall 2024',
                'students': 35,
                'reviews_completed': 35,
                'total_reviews': 35
            },
            {
                'code': 'CSCI1102.02',
                'name': 'Computer Science I',
                'term': 'Fall 2024',
                'students': 32,
                'reviews_completed': 30,
                'total_reviews': 32
            }
        ],
        'forms': [
            {
                'name': 'Delivery 2 Peer Review',
                'class': 'CSCI3356.01',
                'submitted': 29,
                'total': 38,
                'due_date': 'Friday 11:59 PM'
            },
            {
                'name': 'Delivery 2 Peer Review',
                'class': 'CSCI3356.02',
                'submitted': 25,
                'total': 31,
                'due_date': 'Friday 11:59 PM'
            },
            {
                'name': 'Delivery 1 Peer Review',
                'class': 'CSCI3356.01',
                'submitted': 38,
                'total': 38,
                'due_date': '2/14/2025'
            }
        ]
    }
    return render(request, "staff_dashboard.html", context)

@login_required
@user_passes_test(is_student)
def student_dashboard(request):
    context = {
        'username': request.user.username,
        'assigned_tasks': None,  # Will use default in template
        'user_classes': None,    # Will use default in template
        'teams': None           # Will use default in template
    }
    return render(request, "student_dashboard.html", context)
