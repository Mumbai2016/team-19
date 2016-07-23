from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100, blank=True, null=True)

    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=20)
    age = models.DecimalField(max_length=10)

    mobile_no = models.CharField(max_length=14)
    mother_mobile_no = models.CharField(max_length=14, blank=True, null=True)
    father_mobile_no = models.CharField(max_length=14, blank=True, null=True)
    other_no = models.CharField(max_length=14, blank=True, null=True)

    program_start_date = models.CharField(max_length=20, blank=True, null=True)
    program_duration = models.CharField(max_length=20, blank=True, null=True)

    is_active = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    is_deactivated = models.BooleanField(default=False)
    deactivated_on = models.DateTimeField(default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

