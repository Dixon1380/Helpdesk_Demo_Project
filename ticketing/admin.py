from django.contrib import admin
from .models import Ticket



class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'title', 'status', 'priority', 'assigned_agent', 'date_created')
    list_filter = ('status', 'priority', 'assigned_agent')
    search_fields = ('ticket_number', 'title')

admin.site.register(Ticket, TicketAdmin)
