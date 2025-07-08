from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db.models import Avg, Count
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
