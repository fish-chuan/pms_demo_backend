import uuid
from django.db import models


class Member(models.Model):

    GENDER_CHOICE = (
        ("m", "Male"),
        ("f", "Female"),
        ("o", "Other")
    )

    serial_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    card_number = models.CharField(max_length=32, blank=True)
    username = models.CharField(max_length=32)
    gender = models.CharField(choices=GENDER_CHOICE, default="o")
    phone = models.CharField(max_length=32, blank=True)
    address = models.TextField(default="", blank=True)
    photo = models.ImageField(upload_to='profile', blank=True)
    points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "member"


class Plan(models.Model):

    PLAN_CHOICE = (
        ("yearly", "YEARLY"),
        ("half-year", "HALF-YEAR"),
        ("season", "SEASON")
    )

    plan_type = models.CharField(choices=PLAN_CHOICE, blank=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='plan')
    plan_start = models.DateField(auto_now=False)
    plan_end = models.DateField(auto_now=False)
    is_activate = models.BooleanField(default=False)

    class Meta:
        db_table = "plan"
