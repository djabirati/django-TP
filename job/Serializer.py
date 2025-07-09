from rest_framework import serializers
from .models import Contract, Skill, Industry, Candidate, JobRecord


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'type_code', 'description']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ['id', 'name']


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'name', 'email', 'location']


class JobRecordSerializer(serializers.ModelSerializer):
    contract = ContractSerializer(read_only=True)
    skill = SkillSerializer(read_only=True)
    industry = IndustrySerializer(read_only=True)
    candidate = CandidateSerializer(read_only=True)

    class Meta:
        model = JobRecord
        fields = [
            'id',
            'work_year',
            'experience_level',
            'employment_type',
            'job_title',
            'salary',
            'salary_currency',
            'salary_in_usd',
            'employee_residence',
            'remote_ratio',
            'company_location',
            'company_size',
            'contract',
            'skill',
            'industry',
            'candidate',
        ]
