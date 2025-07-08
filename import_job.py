import os
import csv
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myJobProject.settings")
django.setup()

from job.models import JobRecord

csv_path = os.path.join("data", "salaries.csv")
count = 0
line_num = 0

with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        line_num += 1

        job_title = row["job_title"].strip() or "Unknown"
        employee_residence = row["employee_residence"].strip() or "Unknown"
        company_location = row["company_location"].strip() or "Unknown"
        work_year = int(row["work_year"])

        obj, created = JobRecord.objects.get_or_create(
            work_year=work_year,
            job_title=job_title,
            employee_residence=employee_residence,
            company_location=company_location,
            defaults={
                "experience_level": row["experience_level"].strip(),
                "employment_type": row["employment_type"].strip(),
                "salary": int(row["salary"]),
                "salary_currency": row["salary_currency"].strip(),
                "salary_in_usd": int(row["salary_in_usd"]),
                "remote_ratio": int(row["remote_ratio"]),
                "company_size": row["company_size"].strip(),
                "contract": None,
                "industry": None,
                "candidate": None,
                "skill": None
            }
        )

        if created:
            count += 1

        if line_num % 100 == 0:
            print(f"Ligne {line_num} traitée...")

print(f"{count} enregistrements créés dans JobRecord.")
