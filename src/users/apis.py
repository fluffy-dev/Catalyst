from rest_framework import serializers, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from users.services import user_create


class UserCreateApi(APIView):
    """
    API view for creating (registering) a new user.
    Returns an auth token upon successful registration.
    """
    permission_classes = [AllowAny]

    class InputSerializer(serializers.Serializer):
        """
        Input serializer for user creation data.
        """
        email = serializers.EmailField()
        password = serializers.CharField(write_only=True)
        first_name = serializers.CharField(required=False, default="")
        last_name = serializers.CharField(required=False, default="")

    class OutputSerializer(serializers.Serializer):
        """
        Output serializer for returning the auth token.
        """
        token = serializers.CharField()

    def post(self, request) -> Response:
        """
        Handles the POST request to create a new user.
        """
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = user_create(**serializer.validated_data)
        token, _ = Token.objects.get_or_create(user=user)

        output_serializer = self.OutputSerializer({'token': token.key})

        return Response(output_serializer.data, status=status.HTTP_201_CREATED)