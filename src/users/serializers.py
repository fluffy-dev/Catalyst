from rest_framework import serializers


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