from rest_framework import serializers

from famous_persons.models import Person


class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = ('title', 'role_id')
