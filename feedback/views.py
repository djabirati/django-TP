from django.db.models import Avg
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from feedback.Serializer import FeedbackSerializer
from feedback.models import Feedback
from job.models import JobRecord
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

def feedback_list(request, job_id):
    job = get_object_or_404(JobRecord, id=job_id)
    feedbacks = Feedback.objects.filter(job=job)
    min_rating = request.GET.get('min_rating')
    if min_rating:
        feedbacks = feedbacks.filter(rating__gte=min_rating)
    average = feedbacks.aggregate(Avg('rating'))['rating__avg']
    return render(request, 'feedback/feedback_list.html', {
        'feedbacks': feedbacks,
        'average_rating': average,
        'job': job
    })



def add_feedback(request):
    if request.method == 'POST':
        job_id = request.POST.get('job')
        candidate_id = request.POST.get('candidate')
        comment = request.POST.get('comment')
        rating = int(request.POST.get('rating', 0))

        if 1 <= rating <= 5:
            Feedback.objects.create(
                job_id=job_id,
                candidate_id=candidate_id if candidate_id else None,
                comment=comment,
                rating=rating
            )

    return render(request, 'feedback/add_feedback.html')

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['job']
    search_fields = ['comment']
    ordering_fields = ['rating', 'created_at']

