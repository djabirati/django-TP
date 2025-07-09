from django.db.models import Avg
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from feedback.Serializer import FeedbackSerializer
from feedback.models import Feedback
from job.models import JobRecord


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
        author_id = request.POST.get('author_name')
        comment = request.POST.get('comment')
        rating = int(request.POST.get('rating', 0))

        if 1 <= rating <= 5:
            Feedback.objects.create(
                job_id=job_id,
                author_name_id=author_id,
                comment=comment,
                rating=rating
            )

    return render(request, 'feedback/add_feedback.html')

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer