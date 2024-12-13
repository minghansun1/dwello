from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, City

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['income', 'city', 'state']

class UserSignupSerializer(serializers.ModelSerializer):
    income = serializers.DecimalField(max_digits=15, decimal_places=2, required=False)
    city_name = serializers.CharField(write_only=True, required=False)
    state_id = serializers.CharField(max_length=2, write_only=True, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'income', 'city_name', 'state_id']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Remove city_name and state_id from validated_data
        city_name = validated_data.pop('city_name', None)
        state_id = validated_data.pop('state_id', None)
        income = validated_data.pop('income', None)

        # Create the user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        
        # Attempt to get city if city_name and state_id are provided
        city = None
        if city_name and state_id:
            try:
                city = City.objects.get(
                    name__iexact=city_name,
                    state__state_id=state_id.upper()
                )
            except City.DoesNotExist:
                pass  # City not found, continue without setting city

        # Create UserProfile
        UserProfile.objects.create(
            user=user,
            income=income,
            city=city,
        )

        return user
