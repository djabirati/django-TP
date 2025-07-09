from django.urls import path

from . import views


urlpatterns = [
    path('stats/', views.stats_view, name='job-stats'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
]
