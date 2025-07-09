from rest_framework import serializers

from feedback.models import Feedback
from job.Serializer import JobRecordSerializer, CandidateSerializer


class FeedbackSerializer(serializers.ModelSerializer):
    job = JobRecordSerializer(read_only=True)
    author_name = CandidateSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = ['id', 'job', 'author_name', 'comment', 'rating', 'created_at']