from django.contrib.auth.models import AbstractUser
from django.db import models


class Architect(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=255)
    adress = models.CharField(max_length=255, blank=True, null=True)
    region_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(unique=False, max_length=100, default="username")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self) -> str:
        return self.email

    class Meta:
        db_table = "architect"


class QuoteRequest(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=8)
    archi_id = models.ForeignKey(
        Architect, on_delete=models.CASCADE, db_column="archi_id"
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "quote_request"
