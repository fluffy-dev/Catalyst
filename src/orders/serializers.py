from rest_framework import serializers
from orders.models import Ticket

class TicketInputSerializer(serializers.Serializer):
    """
    Serializer for ticket data within an order.
    """
    product_codes = serializers.ListField(child=serializers.CharField())


class OrderInputSerializer(serializers.Serializer):
    """
    Main input serializer for creating an order.
    """
    customer_name = serializers.CharField()
    customer_phone = serializers.CharField()
    comment = serializers.CharField(allow_blank=True, required=False)
    tickets = TicketInputSerializer(many=True, min_length=1)


class TicketStatusInputSerializer(serializers.Serializer):
    """
    Input serializer for updating a ticket's status.
    """
    status = serializers.ChoiceField(choices=Ticket.TicketStatus.choices)