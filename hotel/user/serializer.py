from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password_confirmation=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields=['username','email','password','password_confirmation']
        extra_kwargs={
            'password':{
                'write_only':True
            }
        }
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password_confirmation']

        if password!=password2:
            raise serializers.ValidationError({'error':"password is not same"})
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'Email already exists'})
        
        account = User(email=self.validated_data['email'],username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account
        
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password = serializers.CharField(style={'input_type':'password'},write_only=True)

    def validate(self, data):
        username=data.get('username')
        password=data.get('password')

        if not username or not password:
            raise serializers.ValidationError("Both username and password are required.")
        
        user=authenticate(username=username,password=password)
        if not user:
            raise serializers.ValidationError("Invalid username or password.")
        
        data['user']=user

        return data