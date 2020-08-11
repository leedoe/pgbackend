from django.core import exceptions
from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["pk", "username", "email", "name", "url", "password"]

        extra_kwargs = {
            "url": {"lookup_field": "username"},
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            name=validated_data['name'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        if instance.check_password(validated_data['password']):
            instance.name = validated_data['name']
        else:
            raise exceptions.AuthenticationFailed
        
        instance.save()
        return instance

