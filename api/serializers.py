from blockapp.models import Post
from blockapp.models import User
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['uuid', 'title', 'content', 'created', 'updated']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=100, style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def save(self, **kwargs):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'Password mismatch'})
        
        if User.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({'error': 'username already exits'})
        
        account = User(username=self.validated_data['username'], email=self.validated_data['email'])

        account.set_password(password)

        account.save()

        return account
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if  not username or not password:
            raise serializers.ValidationError({'error': 'Username and password required'})
        
        return data



    


    


