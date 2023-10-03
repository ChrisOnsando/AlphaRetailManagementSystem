from django.urls import path
from accounts.views import (
    SignUpView,
    CashierDeleteView,
    CashierDetailView,
    CashierSignUpView,
    CashierUpdateView,
    CustomerDeleteView,
    CustomerDetailView,
    CustomerSignUpView,
    CustomerUpdateView,
    UserDetailView,
    UserListView,
    UserDeleteView,
    UserUpdateView,
)

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signup/cashier/", CashierSignUpView.as_view(), name="cashier-signup"),
    path("signup/customer/", CustomerSignUpView.as_view(), name="customer-signup"),
    path("users/", UserListView.as_view(), name="users"),
    path("user/<int:pk>/detail/", UserDetailView.as_view(), name="user-detail"),
    path("user/<int:pk>/update/", UserUpdateView.as_view(), name="user-update"),
    path("user/<int:pk>/delete/", UserDeleteView.as_view(), name="user-delete"),
    path("profile/<int:pk>/cashier/", CashierDetailView.as_view(), name="cashier-profile"),
    path("update/<int:pk>/cashier/", CashierUpdateView.as_view(), name="cashier-update"),
    path("delete/<int:pk>/cashier/", CashierDeleteView.as_view(), name="cashier-delete"),
    path(
        "profile/<int:pk>/customer/",
        CustomerDetailView.as_view(),
        name="customer-profile",
    ),
    path(
        "update/<int:pk>/customer/",
        CustomerUpdateView.as_view(),
        name="customer-update",
    ),
    path(
        "delete/<int:pk>/customer/",
        CustomerDeleteView.as_view(),
        name="customer-delete",
    ),
]
