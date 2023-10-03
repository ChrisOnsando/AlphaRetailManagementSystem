from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from accounts.models import User, Cashier, Customer


class CashierSignUpForm(UserCreationForm):
    """
    Extending django's user registration form
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_cashier = True
        user.save()
        cashier = Cashier.objects.create(user=user)
        return user


class CustomerSignUpForm(UserCreationForm):
    """
    Customer sign up form
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        return user
    