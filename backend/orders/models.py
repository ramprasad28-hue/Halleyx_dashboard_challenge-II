from django.db import models

class CustomerOrder(models.Model):
    country_choices = [
        ('USA', 'United States'),
        ('CAN', 'Canada'),
        ('GBR', 'United Kingdom'),
        ('IND', 'India'),
        ('AUS', 'Australia'),
        ('DEU', 'Germany'),
        ('FRA', 'France'),
        ('BRA', 'Brazil'),
        ('JPN', 'Japan'),
        ('ZAF', 'South Africa'),
    ]
    product_choices = [
        ('Laptop', 'Laptop'),
        ('Smartphone', 'Smartphone'),
        ('Headphones', 'Headphones'),
        ('Camera', 'Camera'),
        ('Smartwatch', 'Smartwatch'),
        ('Tablet', 'Tablet'),
        ('Monitor', 'Monitor'),
        ('Printer', 'Printer'),
        ('Keyboard', 'Keyboard'),
        ('Mouse', 'Mouse'),
         ('fiber_300', 'Fiber Internet 300 Mbps'),
        ('5g_unlimited', '5G Unlimited Mobile Plan'),
        ('fiber_1gb', 'Fiber Internet 1 Gbps'),
        ('business_500', 'Business Internet 500 Mbps'),
        ('voip_corporate', 'VoIP Corporate Package'),
    ]
    status_choices = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('cancelled', 'Cancelled'),]
    created_by_choices = [
        ('admin', 'Admin'),
        ('Ramprasad', 'Ramprasad'),
        ('Sabari', 'Sabari'), 
        ('Prabha', 'Prabha'),
        ('Sanjay', 'Sanjay'),]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField()
    phone = models.CharField(max_length=20)
    street_address = models.CharField(max_length=200, blank=True)
    city= models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=10, choices=country_choices)

    product = models.CharField(max_length=100,choices=product_choices)

    quantity = models.IntegerField(default=1)
    unit_price = models.FloatField()
    total_amount = models.FloatField(blank=True)

    status = models.CharField(max_length=50, choices=status_choices)

    created_by = models.CharField(max_length=100, choices=created_by_choices, default='admin')

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_amount = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class DashboardLayout(models.Model):

    layout = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)