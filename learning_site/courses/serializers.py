from rest_framework import serializers
from . import models

class CourseSerializer(serializers.ModelSerializer):
    # in this case, using a StringRelatedField is fine, but in
    # the case of big data HyperlinkedRelatedField is preferred.
    steps = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Course
        fields = (
            'created_at',
            'title',
            'description',
            'pk', # this field is created by Django
            'steps', # "related_name" for relational field
        )
        # this specifies that the email field cannot be read by the user of
        # the API. However, it can be overwritten in the case of a POST request.
        # (Not really necessary here, but shown as an example. For security
        # reasons, sometimes this is necessary).
        extra_kwargs = {
            'email': {'write_only': True}
        }

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Step
        fields = (
            'title',
            'description',
            'content',
            'order',
            'course',
            'pk'
        )
