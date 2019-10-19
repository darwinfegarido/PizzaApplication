from django.contrib import admin

from .models import PizzaType, Pizza, Transaction

admin.site.register(PizzaType)
admin.site.register(Pizza)
admin.site.register(Transaction)
