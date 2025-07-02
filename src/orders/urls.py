from django.urls import path
from orders.apis import OrderCreateApi, TicketStatusUpdateApi

urlpatterns = [
    path('create/', OrderCreateApi.as_view(), name='create'),
    path('tickets/<uuid:ticket_code>/update-status/', TicketStatusUpdateApi.as_view(), name='ticket-update-status'),
]