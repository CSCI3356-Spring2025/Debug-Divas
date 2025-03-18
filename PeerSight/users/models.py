from django.contrib.auth.models import AbstractUser
from django.db import models
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import resolve_url

# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('professor', 'Professor'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    def is_professor(self):
        return self.role == 'professor'

    def is_student(self):
        return self.role == 'student'

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def get_connect_redirect_url(self, request, socialaccount):
        """
        After successful authentication, redirect to home view which will
        then redirect to the appropriate dashboard based on user's role
        """
        return resolve_url('/')
