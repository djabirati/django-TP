from rest_framework import serializers

from feedback.models import Feedback
from job.Serializer import JobRecordSerializer, CandidateSerializer
from job.models import Candidate, JobRecord


class FeedbackSerializer(serializers.ModelSerializer):
    job = JobRecordSerializer(read_only=True)
    candidate = CandidateSerializer(read_only=True)

    job_id = serializers.PrimaryKeyRelatedField(
        queryset=JobRecord.objects.all(),
        source='job',
        write_only=True
    )
    candidate_id = serializers.PrimaryKeyRelatedField(
        queryset=Candidate.objects.all(),
        source='candidate',
        write_only=True,
        required=False
    )

    class Meta:
        model = Feedback
        fields = [
            'id',
            'job', 'job_id',
            'candidate', 'candidate_id',
            'comment',
            'rating',
            'created_at'
        ]