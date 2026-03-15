from django.db import models

class CustomerOrder(models.Model):

    STATUS_CHOICES=[
    ('pending','Pending'),
    ('in_progress','In Progress'),
    ('completed','Completed'),
    ('cancelled','Cancelled'),
    ]

    status=models.CharField(max_length=20,choices=STATUS_CHOICES)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField()
    phone = models.CharField(max_length=20)

    country = models.CharField(max_length=50)

    product = models.CharField(max_length=100)

    quantity = models.IntegerField()
    unit_price = models.FloatField()
    total_amount = models.FloatField(blank=True)

    status = models.CharField(max_length=50)

    created_by = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_amount = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class DashboardLayout(models.Model):

    layout = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)