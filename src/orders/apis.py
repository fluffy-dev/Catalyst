import uuid

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from orders.selectors import ticket_get
from orders.services import order_create, ticket_status_update
from orders.serializers import OrderCreateInputSerializer, TicketStatusUpdateInputSerializer

class OrderCreateApi(APIView):
    """
    API for creating a new order. Requires token authentication.
    """

    def post(self, request) -> Response:
        """
        Handles the POST request to create an order.
        """
        serializer = OrderCreateInputSerializer(data=request.data)
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

    def post(self, request, ticket_code: uuid.UUID) -> Response:
        """
        Handles POST request to update a ticket's status.
        """
        serializer = TicketStatusUpdateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ticket = ticket_get(code=ticket_code)

        ticket_status_update(ticket=ticket, status=serializer.validated_data['status'])

        return Response(status=status.HTTP_200_OK)