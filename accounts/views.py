from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from accounts.models import User, Cashier, Customer
from accounts.forms import CashierSignUpForm, CustomerSignUpForm
from django.contrib.auth import login
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)


class UserListView(UserPassesTestMixin, generic.ListView):
    """admin sees all users"""

    model = User
    template_name = "accounts/users_list.html"
    paginate_by = 6

    def test_func(self):
        return self.request.user.is_staff


class UserDetailView(UserPassesTestMixin, generic.DetailView):
    """details on specific users"""

    model = User
    template_name = "accounts/user_detail.html"

    def test_func(self):
        return self.request.user.is_staff


class UserUpdateView(UserPassesTestMixin, UpdateView):
    """
    admin updates user but only their roles
    """

    model = User
    template_name = "accounts/user_update.html"
    fields = [
        "is_customer",
        "is_cashier",
    ]
    success_url = reverse_lazy("users")

    def test_func(self):
        return self.request.user.is_staff


class UserDeleteView(UserPassesTestMixin, DeleteView):
    """
    admin deletes a user

    """

    model = User
    template_name = "accounts/user_delete.html"
    success_url = reverse_lazy("users")

    def test_func(self):
        return self.request.user.is_staff


class SignUpView(TemplateView):
    """
    Give the option to sign up as a cashier or a customer
    
    """

    template_name = "registration/signup.html"


class CashierSignUpView(CreateView):
    """
    Allow cashiers to sign up

    """

    model = User
    form_class = CashierSignUpForm
    template_name = "registration/signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "cashier"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("index")


class CashierDetailView(LoginRequiredMixin, generic.DetailView):
    """
    Cashier views his/her profile

    """

    model = Cashier
    template_name = "accounts/my_profile.html"


class CashierUpdateView(LoginRequiredMixin, UpdateView):
    """
    Cashier updates their profile

    """

    model = Cashier
    fields = [
        "name",
        "city",
        "address",
        "teller_no",
        "contact",
    ]
    template_name = "accounts/update_profile.html"
    success_url = reverse_lazy("index")


class CashierDeleteView(LoginRequiredMixin, DeleteView):
    """
    Cashier deletes account
    This removes him/her from the system

    """

    model = Cashier
    template_name = "accounts/delete_account.html"
    success_url = reverse_lazy("signup")


class CustomerSignUpView(CreateView):
    """
    Allow customers to sign up

    """

    model = User
    form_class = CustomerSignUpForm
    template_name = "registration/signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "customer"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("index")


class CustomerDetailView(LoginRequiredMixin, generic.DetailView):
    """
    Customer views his/her profile

    """

    model = Customer
    template_name = "accounts/my_profile.html"


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    """
    Customer updates their profile
    """

    model = Customer
    fields = [
        "name",
        "city",
        "address",
    ]
    template_name = "accounts/update_profile.html"
    success_url = reverse_lazy("index")


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    """
    Customer deletes account
    This removes him/her from the database
    """

    model = Customer
    template_name = "accounts/delete_account.html"
    success_url = reverse_lazy("signup")
    