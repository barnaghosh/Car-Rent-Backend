# from django.db.models.base import Model
# from rest_framework.serializers import ModelSerializer
# from CarRentApi.models import UserProfile,Owner,Customer

# class UserProfileSerializer(ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = (
#             "id",
#             "email",
#             "password",
#         )
#         extra_kwargs = {
#             "password": {"write_only": True, "style": {"input_type": "password"}}
#         }
#     def create(self, validated_data):
#         user = UserProfile.objects.create_customer(
#             email=validated_data["email"],
#             password=validated_data["password"],
#         )

#         return user
# class OwnerProfileSerializer(ModelSerializer):
#     userprofile = UserProfileSerializer()

#     class Meta:
#         model = Owner
#         fields = "__all__"
#     def create(self, validated_data):
#         user = UserProfile.objects.create_owner(
#             email=validated_data["email"],
#             password=validated_data["password"],
#         )

#         return user

#     def create(self, validated_data):
#         userprofile_data = validated_data.pop("userprofile")
#         userprofile = UserProfileSerializer.create(
#             UserProfileSerializer(), validated_data=userprofile_data
#         )
        
#         user, created = Owner.objects.update_or_create(
#             userprofile=userprofile,
#         )

#         return user


# class CustomerProfileSerializer(ModelSerializer):
#     # userprofile = UserProfileSerializer()

#     class Meta:
#         model = Customer
#         exclude = [
#             "user",
#         ]
#     # def create(self, validated_data):
#     #     # user = UserProfile.objects.create_customer(
#     #     #     email=validated_data["email"],
#     #     #     password=validated_data["password"],
#     #     # )
#     #     # userprofile_data = validated_data.pop("userprofile")
#     #     # UserProfileSerializer.create(
#     #     #     UserProfileSerializer(), validated_data=userprofile_data
#     #     # )
        
#     #     customer, created =Customer.objects.get_or_create(**validated_data)
#     #     return customer

#     # def create(self, validated_data):
#     #     userprofile_data = validated_data.pop("user")
#     #     userprofile = UserProfileSerializer.create(
#     #         UserProfileSerializer(), validated_data=userprofile_data
#     #     )
        
#     #     customer, created = Owner.objects.update_or_create(
#     #         user=validated_data.pop("user"),
#     #     )

#     #     return customer

# class CustomerUserSerializer(ModelSerializer):
#     customers = CustomerProfileSerializer()

#     class Meta:
#         model = UserProfile
#         fields = "__all__"
#         def create(self, validated_data):
#             customer_data = validated_data.pop("customers")
            
#             customers = CustomerProfileSerializer.create(
#                 CustomerProfileSerializer(), validated_data=customer_data
#             )
            
#             order, created = UserProfile.objects.update_or_create(
#                 price=validated_data.pop("price"),
#                 orderTime=validated_data.pop("orderTime"),
#                 user=validated_data.pop("user"),
#             )

#             return order

# # class OwnerProfileSerializer(ModelSerializer):
# #     class Meta:
# #         model = Owner
# #         fields = (
# #             "id",
# #             "email",
# #             "password",
# #         )
# #         extra_kwargs = {
# #             "password": {"write_only": True, "style": {"input_type": "password"}}
# #         }

# #     def create(self, validated_data):
# #         user = UserProfile.objects.create_owner(
# #             email=validated_data["email"],
# #             password=validated_data["password"],
# #         )

# #         return user


# # class CustomerProfileSerializer(ModelSerializer):
# #     class Meta:
# #         model = Customer
# #         fields = (
# #             "id",
# #             "email",
# #             "password",
# #         )
# #         extra_kwargs = {
# #             "password": {"write_only": True, "style": {"input_type": "password"}}
# #         }

# #     def create(self, validated_data):
# #         user = UserProfile.objects.create_customer(
# #             email=validated_data["email"],
# #             password=validated_data["password"],
# #         )

# #         return user



from rest_framework.serializers import ModelSerializer
from CarRentApi.models import UserProfile,Owner,Customer,Book

class OwnerUserProfileSerializer(ModelSerializer):
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

class CustomerUserProfileSerializer(ModelSerializer):
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

class OwnerProfileSerializer(ModelSerializer):
    user = OwnerUserProfileSerializer()
    

    class Meta:
        model = Owner
        fields = "__all__"

    def create(self, validated_data):
        ingredient_data = validated_data.pop("user")
        ingredients = OwnerUserProfileSerializer.create(
            OwnerUserProfileSerializer(), validated_data=ingredient_data
        )
        order, created = Owner.objects.update_or_create(
            user=ingredients,
        )

        return order

class CustomerProfileSerializer(ModelSerializer):
    user = CustomerUserProfileSerializer()
    

    class Meta:
        model = Customer
        fields = "__all__"

    def create(self, validated_data):
        ingredient_data = validated_data.pop("user")
        ingredients = CustomerUserProfileSerializer.create(
            CustomerUserProfileSerializer(), validated_data=ingredient_data
        )
        order, created = Customer.objects.update_or_create(
            user=ingredients,
        )

        return order

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
    def create(self, validated_data):
        book, created = Book.objects.update_or_create(
            username=validated_data.pop('username'),
            phone=validated_data.pop("phone"),
            roomname=validated_data.pop("roomname"),
            roomtype=validated_data.pop("roomtype"),
            roomno=validated_data.pop("roomno"),
            date=validated_data.pop("date"),
            price=validated_data.pop("price"),
            bookTime=validated_data.pop("bookTime"),
            user=validated_data.pop("user"),
        )
        return book