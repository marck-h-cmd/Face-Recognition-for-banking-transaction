from django.db import models

class Employee(models.Model):
    emplcode = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)  # Ideally hashed

    def __str__(self):
        return f"{self.name} {self.lastname}"

    @classmethod
    def find_by_code(cls, emplcode):
        try:
            return cls.objects.get(emplcode=emplcode)
        except cls.DoesNotExist:
            return None

    @classmethod
    def update(cls, emplcode, **kwargs):
        employee = cls.find_by_code(emplcode)
        if employee:
            for key, value in kwargs.items():
                if hasattr(employee, key):
                    setattr(employee, key, value)
            employee.save()
            return employee
        return None

    @classmethod
    def list_all(cls):
        return cls.objects.all()

    def delete_employee(self):
        self.delete()
