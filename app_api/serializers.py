
from rest_framework import serializers
from app_api.models import TeachersModel


class TeachersSerializer(serializers.HyperlinkedModelSerializer):

    #? it displays the student_id as read only in the API server
    Teachers_id = serializers.ReadOnlyField()
    class Meta:
        model= TeachersModel
        fields = "__all__"




