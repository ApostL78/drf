from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from famous_persons.models import Person
from famous_persons.serializers import ModelPersonSerializer, PersonSerializer


class RawPersonAPIView(APIView):
    def get(self, request):
        persons = Person.objects.all()
        return Response({"posts": PersonSerializer(persons, many=True).data})

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_person = Person.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            role=request.data['role_id']
        )
        return Response({'post': PersonSerializer(new_person).data})


class PersonAPIView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = ModelPersonSerializer
