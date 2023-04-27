from django.db import models


# Create your models here
class Grant_Management(models.Model):
    item = models.CharField(max_length=255)
    category = (
        ("OPPORTUNITY", "Opportunity"),
        ("PROCESS", "Process"),
        ("SUBMITTED", "Submitted"),
    )
    priority = (("HIGH", "High"), ("LOW", "Low"))
    timeline = models.DateField(auto_now_add=True)
    date_of_submission = models.DateTimeField(auto_now_add=True)
    Foundation = models.CharField(max_length=255)
    Amount_Requested = models.IntegerField()
    Amount_Received = models.IntegerField()
    Awarded_Dated = models.DateTimeField(auto_now_add=True)
    Payment_Date = models.DateTimeField(auto_now_add=True)
    Purpose = models.CharField(max_length=300)
    POC_NAME = models.CharField(max_length=255)
    Email = models.EmailField()
    Phone = models.CharField(max_length=255)
    Year_Awarded = models.DateField()
n 