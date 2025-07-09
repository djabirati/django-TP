from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('feedback', views.FeedbackViewSet)

"""
urlpatterns = [
    path('', include(router.urls)),
    path('<int:job_id>/', views.feedback_list, name='feedback_list'),
    path('add/', views.add_feedback, name='add_feedback'),
]
"""


urlpatterns = [
    path('', include(router.urls)),
    path('feedback/<int:job_id>/', views.feedback_list, name='feedback_list'),
    path('feedback/add/', views.add_feedback, name='add_feedback'),
]