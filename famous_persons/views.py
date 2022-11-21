from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from famous_persons.models import Person, Role
from famous_persons.permissions import IsAdminOrReadOnly
from famous_persons.serializers import ModelPersonSerializer, PersonSerializer


class PersonViewSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 10000


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
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = PersonViewSetPagination

    @action(methods=["get"], detail=False, url_path="role-list")
    def role_list(self, request):
        roles = Role.objects.all()
        return Response({"roles": [r.name for r in roles]})

    @action(methods=["get"], detail=True, url_path="role-detail")
    def role_detail(self, request, pk=None):
        if not pk:
            roles = Role.objects.all()
            return Response({"roles": [r.name for r in roles]})
        try:
            role = Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            return Response({"error": "Object does not exists"})
        except Role.MultipleObjectsReturned:
            return Response({"error": f"More then 1 instance have the same pk: {pk}"})
        return Response({"role": role.name})
