from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import feedback_list, add_feedback, FeedbackViewSet

router = DefaultRouter()
router.register('api/feedback', FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('', include(router.urls)),

    path('feedback/<int:job_id>/', feedback_list, name='feedback_list'),
    path('feedback/add/', add_feedback, name='add_feedback'),
]

"""
Ne pas afficher tout les jobs record, 
Il faut un menu deroulant avec les job record title et la on affiche tout les feedbacks 
"""