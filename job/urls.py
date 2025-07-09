

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import JobRecordViewSet, job_list, job_detail, stats_view

# ROUTES REST
router = DefaultRouter()
router.register('api/jobs', JobRecordViewSet, basename='jobs')

urlpatterns = [
    # API REST
    path('', include(router.urls)),

    # VUES HTML
    path('jobs/', job_list, name='job_list'),
    path('jobs/<int:job_id>/', job_detail, name='job_detail'),
    path('stats/', stats_view, name='job-stats'),
]