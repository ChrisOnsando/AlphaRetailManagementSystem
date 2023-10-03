from django.contrib import admin
from accounts.models import User, Cashier, Customer

admin.site.register(User)
admin.site.register(Cashier)
admin.site.register(Customer)
