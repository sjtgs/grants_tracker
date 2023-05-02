from django.db import models


# Create your models here


class Category(models.Model):
    category_name = models.CharField(max_length=30)
    parent = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.category_name


class Priority(models.Model):
    priority_name = models.CharField(max_length=30)
    parent = models.ForeignKey("Priority", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.priority_name


class Grant_Management(models.Model):
    item = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
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
    Year_Awarded = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item
