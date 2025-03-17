from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("logout", views.logout_view, name="logout"),
    path("staff-dashboard/", views.staff_dashboard, name="staff_dashboard"),
    path("student-dashboard/", views.student_dashboard, name="student_dashboard"),
]