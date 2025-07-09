from django.urls import path

from . import views

urlpatterns = [
    path('<int:job_id>/', views.feedback_list, name='feedback_list'),
    path('add/', views.add_feedback, name='add_feedback'),
]