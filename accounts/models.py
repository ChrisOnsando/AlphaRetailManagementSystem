from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Extending django user model to add roles
    Registration of users
    
    """

    email = models.EmailField(
        _("email address"),
    )
    is_cashier = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("user-detail", args=[str(self.id)])


class Cashier(models.Model):
    """
    Store cashier details.
   
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(
        max_length=300,
    )
    city = models.CharField(
        max_length=300,
    )
    address = models.CharField(
        max_length=300,
    )
    teller_no = models.PositiveIntegerField(null=True, blank=True)
    contact = models.PositiveIntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("cashier-profile", args=[str(self.id)])

    def __str__(self) -> str:
        return self.user.username


class Customer(models.Model):
    """
    Store customers details.
    Ease in ordering products

    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(
        max_length=300,
    )
    city = models.CharField(
        max_length=300,
    )
    address = models.CharField(
        max_length=300,
    )

    def get_absolute_url(self):
        return reverse("customer-profile", args=[str(self.id)])

    def __str__(self) -> str:
        return self.user.username
    