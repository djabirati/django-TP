from django.contrib import admin

from job.models import Skill, Industry, Candidate, JobRecord, Contract, Category

# Register your models here.
admin.site.register(Skill)
admin.site.register(Industry)
admin.site.register(Candidate)
admin.site.register(JobRecord)
admin.site.register(Contract)
admin.site.register(Category)