
from rest_framework import serializers
from app_api.models import StudentModel


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= StudentModel
        fields = "__all__"

        