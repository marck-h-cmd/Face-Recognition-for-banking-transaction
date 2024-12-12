from django.db import models
from django.contrib.auth.models import User


'''
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    clcode = models.CharField(max_length=10, unique=True)  
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    date_of_birth = models.DateField()
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
    def find_by_face_id(cls,  faceid):
        try:
            return cls.objects.get( faceid= faceid)
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


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emplcode = models.CharField(max_length=10, unique=True)  
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.lastname} ({'Admin' if self.is_admin else 'Employee'})"
    

    def save_employee(self):
        self.save()

    @classmethod
    def find_by_emplcode(cls, emplcode):
        
        return cls.objects.filter(emplcode=emplcode).first()

    @classmethod
    def update_employee(cls, emplcode, updates):   
        employee = cls.objects.filter(emplcode=emplcode).first()
        if employee:
            for key, value in updates.items():
                setattr(employee, key, value)
            employee.save()
            return employee
        return None

    @classmethod
    def delete_employee(cls, emplcode):
      
        return cls.objects.filter(emplcode=emplcode).delete()


'''