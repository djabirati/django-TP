import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myJobProject.settings')
django.setup()


from django.db.models import Avg, Count
from job.models import JobRecord

# 1. Top 5 job titles with highest average USD salary
top_5_jobs = (
    JobRecord.objects
    .values('job_title')
    .annotate(avg_salary=Avg('salary_in_usd'))
    .order_by('-avg_salary')[:5]
)

# 2. Average salary by experience level
avg_salary_by_exp = (
    JobRecord.objects
    .values('experience_level')
    .annotate(avg_salary=Avg('salary_in_usd'))
    .order_by('experience_level')
)

# 3. Number of jobs by company_location
jobs_by_location = (
    JobRecord.objects
    .values('company_location')
    .annotate(count=Count('id'))
    .order_by('-count')
)

# 4. Ratio of 100% remote jobs
total_jobs = JobRecord.objects.count()
remote_jobs = JobRecord.objects.filter(remote_ratio=100).count()
remote_ratio = (remote_jobs / total_jobs) * 100 if total_jobs > 0 else 0


output_path = os.path.join("data", "job_stats.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write("Top 5 job titles with highest average USD salary:\n")
    for job in top_5_jobs:
        line = f"- {job['job_title']}: {round(job['avg_salary'], 2)} USD\n"
        f.write(line)
        print(line, end="")

    f.write("\nAverage salary by experience level:\n")
    for row in avg_salary_by_exp:
        line = f"- {row['experience_level']}: {round(row['avg_salary'], 2)} USD\n"
        f.write(line)
        print(line, end="")

    f.write("\nNumber of jobs per company location:\n")
    for row in jobs_by_location:
        line = f"- {row['company_location']}: {row['count']} jobs\n"
        f.write(line)
        print(line, end="")

    f.write(f"\nRatio of 100% remote jobs: {round(remote_ratio, 2)}%\n")
    print(f"\nRatio of 100% remote jobs: {round(remote_ratio, 2)}%")