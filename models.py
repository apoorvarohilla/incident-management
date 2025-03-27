import uuid
import random
import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User Model
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    pin_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number', 'address', 'pin_code', 'city', 'country']

    def __str__(self):
        return self.username

# Function to generate unique Incident ID
def generate_incident_id():
    current_year = datetime.datetime.now().year
    random_number = random.randint(10000, 99999)
    return f"RMG{random_number}{current_year}"

# Incident Model
class Incident(models.Model):
    INCIDENT_TYPE_CHOICES = [
        ('Enterprise', 'Enterprise'),
        ('Government', 'Government'),
    ]
    
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]

    incident_id = models.CharField(max_length=20, unique=True, default=generate_incident_id, editable=False)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incidents")
    incident_type = models.CharField(max_length=20, choices=INCIDENT_TYPE_CHOICES)
    details = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')

    def __str__(self):
        return f"{self.incident_id} - {self.reporter.username}"
