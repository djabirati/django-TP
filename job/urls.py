

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import JobRecordViewSet

router = DefaultRouter()
router.register('jobs', JobRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('stats/', views.stats_view, name='job-stats'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
]
