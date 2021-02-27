from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    some_serializer_field = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "some_serializer_field",
            "some_model_field",
        ]
        read_only_fields = [
            "some_model_field",
        ]

    def create(self, validated_data):
        some_serializer_field = validated_data.pop("some_serializer_field")

        return User.objects.create(
            **validated_data,
            some_model_field=f"(Model) {some_serializer_field}",
        )
