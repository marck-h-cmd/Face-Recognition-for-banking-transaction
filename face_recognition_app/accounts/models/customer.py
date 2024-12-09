from django.db import models

class Customer(models.Model):
    clcode = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} {self.lastname}"

    @classmethod
    def find_by_code(cls, clcode):
        try:
            return cls.objects.get(clcode=clcode)
        except cls.DoesNotExist:
            return None

    @classmethod
    def update(cls, clcode, **kwargs):
        customer = cls.find_by_code(clcode)
        if customer:
            for key, value in kwargs.items():
                if hasattr(customer, key):
                    setattr(customer, key, value)
            customer.save()
            return customer
        return None

    @classmethod
    def list_all(cls):
        return cls.objects.all()

    def delete_customer(self):
        self.delete()
