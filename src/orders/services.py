from typing import Any, Dict, List

from django.db import transaction

from orders.models import Order, Ticket
from users.models import User


@transaction.atomic
def order_create(*, user: User, customer_name: str, customer_phone: str,
                 comment: str, tickets_data: List[Dict[str, Any]]) -> Order:
    """
    Creates an order with its associated tickets.

    Args:
        user: The user placing the order.
        customer_name: The name of the customer.
        customer_phone: The phone number of the customer.
        comment: A comment for the order.
        tickets_data: A list of dictionaries, each containing data for a ticket.

    Returns:
        The created Order instance.
    """
    order = Order.objects.create(
        user=user,
        customer_name=customer_name,
        customer_phone=customer_phone,
        comment=comment
    )

    for ticket_data in tickets_data:
        Ticket.objects.create(order=order, product_codes=ticket_data['product_codes'])

    return order


@transaction.atomic
def ticket_status_update(*, ticket: Ticket, status: str) -> Ticket:
    """
    Updates the status of a single ticket.

    Args:
        ticket: The Ticket instance to update.
        status: The new status for the ticket.

    Returns:
        The updated Ticket instance.
    """
    ticket.status = status
    ticket.full_clean()
    ticket.save(update_fields=['status', 'updated_at'])

    return ticket