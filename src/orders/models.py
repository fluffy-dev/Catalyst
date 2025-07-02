import uuid

from django.conf import settings
from django.db import models

from src.core.models import BaseModel


class Order(BaseModel):
    """
    Represents a customer order.
    """
    class OrderStatus(models.TextChoices):
        PENDING = 'PENDING', 'В ожидании'
        PROCESSING = 'PROCESSING', 'В обработке'
        COMPLETED = 'COMPLETED', 'Завершен'
        CANCELLED = 'CANCELLED', 'Отменен'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='orders'
    )
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=20)
    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
    )
    comment = models.TextField(blank=True)

    def __str__(self) -> str:
        """
        String representation of the Order model.
        """
        return f"Order {self.id} for {self.customer_name}"


class Ticket(BaseModel):
    """
    Represents a single ticket within an order.
    """
    class TicketStatus(models.TextChoices):
        NEW = 'NEW', 'Новый'
        IN_PROGRESS = 'IN_PROGRESS', 'В работе'
        DONE = 'DONE', 'Выполнен'
        ERROR = 'ERROR', 'Ошибка'

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='tickets'
    )
    code = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    status = models.CharField(
        max_length=20,
        choices=TicketStatus.choices,
        default=TicketStatus.NEW
    )
    product_codes = models.JSONField(default=list)

    def __str__(self) -> str:
        """
        String representation of the Ticket model.
        """
        return f"Ticket {self.code} [{self.status}]"