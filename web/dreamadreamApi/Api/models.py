from django.db import models


class Member(models.Model):
    full_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=32)
    address = models.CharField(max_length=255)


    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=20)
    age = models.DecimalField(max_digits=2, decimal_places=0)

    mobile_no = models.CharField(max_length=14)
    mother_mobile_no = models.CharField(max_length=14, blank=True, null=True)
    father_mobile_no = models.CharField(max_length=14, blank=True, null=True)
    other_no = models.CharField(max_length=14, blank=True, null=True)

    qualification = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    goal = models.CharField(max_length=255)

    program_start_date = models.CharField(max_length=20, blank=True, null=True)
    program_duration = models.CharField(max_length=20, blank=True, null=True)

    is_active = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    is_deactivated = models.BooleanField(default=False)
    deactivated_on = models.DateTimeField(default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    age_min = models.DecimalField(max_digits=2, decimal_places=0)
    age_max = models.DecimalField(max_digits=2, decimal_places=0)


class Call(models.Model):
    member = models.ManyToManyField(Member, related_name="member", null=True, default=None)
    call_date = models.CharField(max_length=20)
    status_at_date = models.CharField(max_length=255)


class Request(models.Model):
    member = models.ManyToManyRel(Member, related_name="member", null=True, default=None)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Event_Registration(models.Model):
    member = models.ForeignKey(Member, related_name="registered_member")
    registered_event = models.ForeignKey(Event, related_name="registered_event")


