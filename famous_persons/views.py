from rest_framework import generics

from famous_persons.models import Person
from famous_persons.serializers import PersonSerializer


class PersonAPIView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
