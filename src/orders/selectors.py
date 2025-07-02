from orders.models import Ticket
import uuid

from django.shortcuts import get_object_or_404



def ticket_get(*, code: uuid.UUID) -> "Ticket":
    """
    Retrieves a ticket by its unique code.

    Args:
        code: The unique code of the ticket.

    Returns:
        The fetched Ticket instance.
    """
    return get_object_or_404(Ticket, code=code)