from rest_framework import serializers
from .models import  Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["id", "file_id", "model_id", "pre_process", "solution_process", "post_process", "fatigue_process",
                  "fracture_process"]




