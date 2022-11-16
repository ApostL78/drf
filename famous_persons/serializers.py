from rest_framework import serializers

from famous_persons.models import Person


class PersonSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    role_id = serializers.IntegerField()


class ModelPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('title', 'role_id')
