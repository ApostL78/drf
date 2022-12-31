from django.contrib.auth.models import User
from rest_framework import serializers

from famous_persons.models import Person, Role


class PersonSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    role_id = serializers.IntegerField()

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get(
            "is_published", instance.is_published
        )
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance


class ModelRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ("name",)


class ModelUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "date_joined")


class ModelPersonSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_info = serializers.SerializerMethodField()
    role_info = serializers.SerializerMethodField()

    def get_user_info(self, instance):
        return ModelUserSerializer(instance.user).data

    def get_role_info(self, instance):
        return ModelRoleSerializer(instance.role).data

    class Meta:
        model = Person
        fields = (
            "pk",
            "title",
            "role_id",
            'role_info',
            "content",
            "time_create",
            "time_update",
            "is_published",
            "user_id",
            "user_info",
            "user",
        )
