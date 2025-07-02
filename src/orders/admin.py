from django.contrib import admin

from orders.models import Order, Ticket


class TicketInline(admin.TabularInline):
    """
    Inline admin view for Tickets within the Order admin page.
    """
    model = Ticket
    extra = 1
    readonly_fields = ('code', 'created_at', 'updated_at')
    fields = ('product_codes', 'status', 'code', 'created_at', 'updated_at')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Order model.
    """
    list_display = ('id', 'customer_name', 'customer_phone', 'status', 'user', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer_name', 'customer_phone', 'user__email')
    inlines = [TicketInline]
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    """
    Admin configuration for the standalone Ticket model.
    """
    list_display = ('code', 'order', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('code', 'order__customer_name')
    readonly_fields = ('code', 'created_at', 'updated_at')