import uuid

from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from src.orders.models import Ticket
from src.orders.selectors import ticket_get
from src.orders.services import order_create, ticket_status_update


class OrderCreateApi(APIView):
    """
    API for creating a new order. Requires token authentication.
    """
    class TicketInputSerializer(serializers.Serializer):
        """
        Serializer for ticket data within an order.
        """
        product_codes = serializers.ListField(child=serializers.CharField())

    class InputSerializer(serializers.Serializer):
        """
        Main input serializer for creating an order.
        """
        customer_name = serializers.CharField()
        customer_phone = serializers.CharField()
        comment = serializers.CharField(allow_blank=True, required=False)
        tickets = TicketInputSerializer(many=True, min_length=1)

    def post(self, request) -> Response:
        """
        Handles the POST request to create an order.
        """
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        order = order_create(
            user=request.user,
            customer_name=validated_data['customer_name'],
            customer_phone=validated_data['customer_phone'],
            comment=validated_data.get('comment', ''),
            tickets_data=validated_data['tickets']
        )

        return Response({'order_id': order.id}, status=status.HTTP_201_CREATED)


class TicketStatusUpdateApi(APIView):
    """
    API for external systems to update the status of a ticket.
    Does not require authentication for demonstration purposes.
    """
    permission_classes = [AllowAny]

    class InputSerializer(serializers.Serializer):
        """
        Input serializer for updating a ticket's status.
        """
        status = serializers.ChoiceField(choices=Ticket.TicketStatus.choices)

    def post(self, request, ticket_code: uuid.UUID) -> Response:
        """
        Handles POST request to update a ticket's status.
        """
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ticket = ticket_get(code=ticket_code)

        ticket_status_update(ticket=ticket, status=serializer.validated_data['status'])

        return Response(status=status.HTTP_200_OK)