
from rest_framework import serializers
from app_api.models import StudentModel


class StudentSerializer(serializers.HyperlinkedModelSerializer):

    #? it displays the student_id as read only in the API server
    Student_id = serializers.ReadOnlyField()
    class Meta:
        model= StudentModel
        fields = "__all__"




