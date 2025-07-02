from typing import TYPE_CHECKING
import uuid

from django.shortcuts import get_object_or_404

if TYPE_CHECKING:
    from src.orders.models import Ticket


def ticket_get(*, code: uuid.UUID) -> "Ticket":
    """
    Retrieves a ticket by its unique code.

    Args:
        code: The unique code of the ticket.

    Returns:
        The fetched Ticket instance.
    """
    return get_object_or_404(Ticket, code=code)