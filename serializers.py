from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Incident

User = get_user_model()

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'address', 'pin_code', 'city', 'country']

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'phone_number', 'address', 'pin_code', 'city', 'country']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data['phone_number'],
            address=validated_data['address'],
            pin_code=validated_data['pin_code'],
            city=validated_data['city'],
            country=validated_data['country']
        )
        return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

# Incident Serializer
class IncidentSerializer(serializers.ModelSerializer):
    reporter_name = serializers.ReadOnlyField(source='reporter.username')

    class Meta:
        model = Incident
        fields = ['incident_id', 'reporter', 'reporter_name', 'incident_type', 'details', 'reported_at', 'priority', 'status']
        read_only_fields = ['incident_id', 'reporter', 'reported_at']

    def validate_status(self, value):
        """Ensure a closed incident cannot be modified"""
        if self.instance and self.instance.status == "Closed":
            raise serializers.ValidationError("Closed incidents cannot be modified.")
        return value
