from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Donor(models.Model):
    # Link donor to a user account (optional)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # Donor details
    donor_name = models.CharField(max_length=100)
    donor_email = models.EmailField(unique=True)

    # Restricting donor blood type choices
    BLOOD_TYPES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B-'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
    ]
    donor_bloodtype = models.CharField(max_length=3, choices=BLOOD_TYPES)

    # Validating phone numbers (only digits allowed)
    donor_phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\d{10,15}$', message="Enter a valid phone number.")]
    )

    # City with a default value
    donor_city = models.CharField(max_length=50, default="Thane")

    def __str__(self):
        return f"{self.donor_name} ({self.donor_bloodtype})"


# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.
# class Donor(models.Model):
#     user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
#     donor_name = models.CharField(max_length=100)
#     donor_email= models.EmailField(unique=True)
#     donor_bloodtype = models.CharField(max_length=3)
#     donor_phone = models.CharField(max_length=15)
#     donor_city = models.CharField(max_length=15 , default="Thane")

