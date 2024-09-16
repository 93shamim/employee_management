from django.db import models
from django.contrib.auth.models import User

DESIGNATION_CHOICES = [
        ('Manager', 'Manager'),
        ('Team Lead', 'Team Lead'),
        ('Developer', 'Developer'),
        ('Tester', 'Tester'),
        ('HR', 'HR'),
        
    ]

class Employee(models.Model):
    empID = models.PositiveIntegerField(unique=True, null=True, editable=False)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    designation = models.CharField(max_length=50,choices=DESIGNATION_CHOICES)
    short_description = models.TextField()

    
    def save(self, *args, **kwargs):
        # Auto-generate empID if not provided
        if not self.empID:
            last_emp = Employee.objects.order_by('empID').last()
            if last_emp:
                self.empID = last_emp.empID + 1
            else:
                self.empID = 1001  # Start from 1001 if no employees exist

        # Create or update a corresponding User object with empID as both username and password
        user, created = User.objects.get_or_create(username=str(self.empID))
        if created:
            # Set the password to empID
            user.set_password(str(self.empID))
            user.save()

        super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        # Delete the associated User object when the employee is deleted
        try:
            user = User.objects.get(username=str(self.empID))
            user.delete()
        except User.DoesNotExist:
            pass  # Handle case if user doesn't exist for some reason

        super().delete(*args, **kwargs)
        

    def __str__(self):
        return self.name