from rest_framework.serializers import ModelSerializer
from CarRentApi.models import UserProfile


class OwnerProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "email",
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        user = UserProfile.objects.create_owner(
            email=validated_data["email"],
            password=validated_data["password"],
        )

        return user


class CustomerProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "email",
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        user = UserProfile.objects.create_customer(
            email=validated_data["email"],
            password=validated_data["password"],
        )

        return user
