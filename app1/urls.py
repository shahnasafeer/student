from django.urls import path
from .views import StudentView, StudentDetailView

urlpatterns = [
    path('students/', StudentView.as_view(), name='students_list'),
    path('students/<int:id>/', StudentDetailView.as_view(), name='student_detail'),
]
