from rest_framework import serializers
from user.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'photo_profile', 'name', 'fullName', 'userPlaceOfStudy', 'type_user']