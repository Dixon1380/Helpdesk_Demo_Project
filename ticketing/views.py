from django.views.generic import ListView, DetailView
from .models import Ticket

class TicketListView(ListView):
    model = Ticket
    template_name = 'ticket_list.html'
    context_object_name = 'tickets'

class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'ticket_detail.html'
    context_object_name = 'ticket'
