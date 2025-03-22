from rest_framework import generics, status
from .serializers import PostSerializer, UserSerializer, LoginSerializer
from blockapp.models import Post, User
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'message': 'Account successfully created'
        })

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user :
                login(request, user)

                token, created = Token.objects.get_or_create(user=user)

                return Response({
                    'message': 'Login successful',
                    'token': token.key
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'message': 'Login failed'
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'message': 'Invalid credentials'
            }, status=status.HTTP_400_BAD_REQUEST)
 
class logoutView(generics.GenericAPIView):
    def get(self, request):
        logout(request)
        return Response({
            'message': 'Logout successful'
        }, status=status.HTTP_200_OK)
    




        
