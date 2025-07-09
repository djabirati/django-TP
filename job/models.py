from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Contract(models.Model):
    type_code = models.IntegerField()
    description = models.TextField()

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Industry(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=100)


class JobRecord(models.Model):
    work_year = models.IntegerField()
    experience_level = models.CharField(max_length=2)
    employment_type = models.CharField(max_length=2)
    job_title = models.CharField(max_length=100)
    salary = models.IntegerField()
    salary_currency = models.CharField(max_length=3)
    salary_in_usd = models.IntegerField()
    employee_residence = models.CharField(max_length=2)
    remote_ratio =models.IntegerField()
    company_location = models.CharField(max_length=2)
    company_size = models.CharField(max_length=1)
    contract = models.ForeignKey(
        Contract,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    industry = models.ForeignKey(
        Industry,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )