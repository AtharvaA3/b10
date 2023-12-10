from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100 , unique=True)
    mob_no = models.IntegerField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    salary = models.IntegerField(default=8500)

    def __str__(self):
        return f"{self.first_name}"
    
class Product(models.Model):
    name = models.CharField(max_length=50)

    # if we don't want to create table then  we add this 
    class Meta:
        abstract = True
    


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.first_name}"
    
    #to work as a alter query aaplyala jr table name edit krych asl tr
    class Meta: 
        db_table = "person"
    

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL,null=True)  #if person is to be deleted then person id cha row delete nhi honar toh null rahnar
    # Add other fields specific to the Address model

    # Define a foreign key relationship to the Person model
    # person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='addresses')

    def __str__(self):
        return f"{self.street}"
    
    class Meta:
        db_table = "address"
    

class Profile(models.Model):
    bio = models.TextField()
    date_of_birth = models.DateField()
    person = models.OneToOneField(Person,on_delete=models.CASCADE)   #person_id we define here // also define one to one relationship

    def __str__(self):
        return f"{self.bio}"

# ORM    :- Object relational Mapper- Object Oriented API

# Employee.objects.all()  


# -----------------------------------------------------------------

#many to mamy relationship


class FuelType(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

    class Meta:
        db_table = "fuel"
    
    
class CarModel(models.Model):
    name = models.CharField(max_length=255)
    fueltype = models.ManyToManyField(FuelType,related_name='models')                #we can take this relation with the fuel also

    def __str__(self):
        return self.name
    

    class Meta:
        db_table = "car"