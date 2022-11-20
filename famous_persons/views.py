from rest_framework import viewsets
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
        serializer.save()

        return Response({"post": serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "instance can't be defined (provide a pk)"})

        try:
            instance = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response({"error": "Object does not exists"})
        except Person.MultipleObjectsReturned:
            return Response({"error": f"More then 1 instance have the same pk: {pk}"})

        serializer = PersonSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "instance can't be defined (provide a pk)"})

        try:
            instance = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response({"error": "Object does not exists"})
        except Person.MultipleObjectsReturned:
            return Response({"error": f"More then 1 instance have the same pk: {pk}"})

        instance.delete()

        return Response({"post": "delete post " + str(pk)})


# class PersonListAPIView(generics.ListAPIView):
#     queryset = Person.objects.all()
#     serializer_class = ModelPersonSerializer
#
#
# class PersonListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = ModelPersonSerializer
#
#
# class PersonCRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = ModelPersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = ModelPersonSerializer
