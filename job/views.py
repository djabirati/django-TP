from django.contrib.auth.models import Permission
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.db.models import Avg, Count
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .Serializer import JobRecordSerializer
from .models import JobRecord

def stats_view(request):
    total_jobs = JobRecord.objects.count()
    avg_salary = JobRecord.objects.aggregate(Avg('salary_in_usd'))['salary_in_usd__avg'] or 0
    total_countries = JobRecord.objects.values('employee_residence').distinct().count()

    context = {
        'total_jobs': total_jobs,
        'avg_salary': round(avg_salary, 2),
        'total_countries': total_countries,
    }

    return render(request, 'job/stats.html', context)

def job_list(request):
    selected_title = request.GET.get('job_title')
    if selected_title:
        jobs = JobRecord.objects.filter(job_title=selected_title)
    else:
        jobs = []  # Vide si rien sélectionné

    all_titles = JobRecord.objects.values_list('job_title', flat=True).distinct()

    return render(request, 'job/job_list.html', {
        'jobs': jobs,
        'all_titles': all_titles,
        'selected_title': selected_title
    })

def job_detail(request, job_id):
    job = get_object_or_404(JobRecord, id=job_id)
    return render(request, 'job/job_detail.html', {'job': job})

class JobRecordViewSet(viewsets.ModelViewSet):
    queryset = JobRecord.objects.all()
    serializer_class = JobRecordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['job_title', 'employee_residence']
    ordering_fields = ['salary_in_usd']