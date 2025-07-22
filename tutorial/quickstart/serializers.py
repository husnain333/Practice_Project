from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']  
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create_user(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']
