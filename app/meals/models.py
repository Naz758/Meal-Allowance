from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class User(AbstractUser):
    can_add_claim = models.BooleanField(default=True)
    can_approve_calm = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class Position(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="staff")
    full_name = models.CharField(max_length=100, unique=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "staff"

    def __str__(self):
        if self.full_name:
            return self.full_name
        return self.user.username


class ClaimAmount(models.Model):
    amount = models.PositiveIntegerField(default=25)

    class Meta:
        verbose_name_plural = "claim amount"

    def __str__(self):
        return f"${self.amount}"


class Claim(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    amount = models.ForeignKey(ClaimAmount, on_delete=models.SET_DEFAULT, default=1)
    purpose = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("meals:claim-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.staff.full_name} {self.amount}"


class ClaimApprover(models.Model):
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
    approver = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.claim} approved by {self.approver}"
