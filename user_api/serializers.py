from rest_framework import serializers
from user.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_no', 'first_name', 'last_name', 'terms_agree', 'remember_me', 'user_type']

    def create(self, validated_data):
        # Ensure the user_type is set, defaulting to 'normal' if not provided
        user_type = validated_data.get('user_type', 'normal')
        user = CustomUser.objects.create(**validated_data)
        user.user_type = user_type
        user.save()
        return user
    
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile_picture']  # Add your custom fields here

