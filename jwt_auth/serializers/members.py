# here
import django.contrib.auth.password_validation as validations
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

User = get_user_model()


class CommonUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.pop("password")
        password_confirmation = data.pop("password_confirmation")
        if password != password_confirmation:
            raise serializers.ValidationError({"password_confirmation": "Passwords do not match"})
        try:
            validations.validate_password(password=password)
        except ValidationError as err:
            raise serializers.ValidationError({"password": err.messages})
        data["password"] = make_password(password)
        return data

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "password_confirmation",
            "email",
            "name",
            "debt",
            "squads",
            "admin_squads",
            "attending",
            "squad_requests",
        )
