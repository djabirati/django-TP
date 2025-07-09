from django.db.models import Avg
from django.shortcuts import render

from feedback.models import Feedback


# Create your views here.

def feedback_list(request, job_id):
    min_rating = request.GET.get('min_rating')
    feedbacks = Feedback.objects.filter(job_id=job_id)
    if min_rating:
        feedbacks = feedbacks.filter(rating__gte=min_rating)
    average = feedbacks.aggregate(Avg('rating'))['rating__avg']
    return render(request, 'feedback/feedback_list.html', {
        'feedbacks': feedbacks,
        'average_rating': average
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

