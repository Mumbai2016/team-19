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

    goal = models.CharField(max_length=255, blank=True, null=True)

    reward_points = models.CharField(max_length=255, blank=True, null=True)

    program_start_date = models.CharField(max_length=20, blank=True, null=True, default=None)
    program_duration = models.CharField(max_length=20, blank=True, null=True, default=None)

    is_active = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    is_deactivated = models.BooleanField(default=False)
    deactivated_on = models.DateTimeField(default=None, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Call(models.Model):
    mobile_no = models.CharField(max_length=100, null=True, blank=True)
    response = models.CharField(max_length=100, null=True, blank=True)
    callsid = models.CharField(max_length=100, null=False, blank=False)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    duration = models.FloatField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'api'


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    age_min = models.DecimalField(max_digits=2, decimal_places=0)
    age_max = models.DecimalField(max_digits=2, decimal_places=0)
    is_disabled = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EventRegistration(models.Model):
    member = models.ForeignKey(Member, related_name="registered_member")
    registered_event = models.ForeignKey(Event, related_name="registered_event")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Feedback(models.Model):
    member = models.ForeignKey(Member, related_name="feedback_member")
    event = models.ForeignKey(Event, related_name="feedback_event")
    feedback = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Request(models.Model):
    member = models.ManyToManyField(Member, related_name="request_member", default=None)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Status(models.Model):
    member = models.ManyToManyField(Member, related_name="member", null=True, default=None)
    status_date = models.DateField(default=None)
    qualification_status = models.CharField(max_length=255)
    employment_status = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)