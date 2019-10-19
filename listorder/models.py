from django.db import models

class PizzaType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    pizza_type_id = models.ForeignKey(PizzaType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return "{0} - {1}".format(self.name, self.price)


class Transaction(models.Model):
    pizza_id = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return "{0} - {1}".format(self.pizza_id, self.quantity)
