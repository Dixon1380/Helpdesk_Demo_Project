from django.db import models
from django.contrib.auth.models import User


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    department = models.CharField(max_length=200)

    def __str__(self):
        return self.user



class Ticket(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    PROIRITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]
    ticket_number = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=20, choices=PROIRITY_CHOICES)
    assigned_agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def generate_ticket_number(self):
        prefix = "Ticket# "
        last_ticket = Ticket.objects.order_by('id').first()
        if last_ticket:
            last_ticket_number = int(last_ticket.ticket_number.split(prefix))
            new_ticket_number = last_ticket_number + 1
        else:
            new_ticket_number = 1
        return f"{prefix}{new_ticket_number:04d}"
    
    def save(self, *args, **kwargs):
        if not self.ticket_number:
            self.ticket_number = self.generate_ticket_number()
        super().save(*args, **kwargs)
   
    def __str__(self):
        return f"Ticket #{self.id} - {self.title[:50]}"