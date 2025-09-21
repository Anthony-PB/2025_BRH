from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer
# Make sure this import path matches your project structure
from aggregator.models import Source
# Make sure this import path matches your project structure
from aggregator.models import Source

User = get_user_model()



class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            # Create authentication token
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({
                'message': 'User created successfully',
                'user': {
                    'id': str(user.id),
                    'email': user.email,
                    'display_name': getattr(user, 'display_name', ''),
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                },
                'token': token.key  # Add this line
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserRegistrationSerializer
    
    def get_object(self):
        """
        Override this method to ensure users can only
        view, update, or delete their own profile.
        """
        return self.request.user

    def destroy(self, request, *args, **kwargs):
        """
        Custom logic for when a user is deleted.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        # You can add custom logic here, like logging out the user
        # TODO: Think about logging out?
        return Response(
            {"message": "User deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )

class FollowSourceView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, source_id):
        user = request.user
        if not Source.objects.filter(id=source_id).exists():
            return Response({'error': 'Source not found'}, status=status.HTTP_404_NOT_FOUND)

        user.follow_source(source_id)
        return Response({'message': 'Source followed successfully'}, status=status.HTTP_200_OK)


class UnfollowSourceView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, source_id):
        user = request.user
        if not Source.objects.filter(id=source_id).exists():
            return Response({'error': 'Source not found'}, status=status.HTTP_404_NOT_FOUND)

        user.unfollow_source(source_id)
        return Response({'message': 'Source unfollowed successfully'}, status=status.HTTP_200_OK)
