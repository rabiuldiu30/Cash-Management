from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    def __str__(self):
        return str(self.username)


class AddCashModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    source = models.CharField(max_length=200,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField(default=0)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user}-{self.amount}"

class ExpenseModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True, blank=True)
    amount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"