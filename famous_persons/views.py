from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from famous_persons.models import Person
from famous_persons.serializers import PersonSerializer


class RawPersonAPIView(APIView):
    def get(self, request):
        persons = Person.objects.all().values()
        return Response({"posts": list(persons)})

    def post(self, request):
        new_person = Person.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            role=request.data['role_id']
        )
        return Response({'post': model_to_dict(new_person)})


class PersonAPIView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
