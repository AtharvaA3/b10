from app.models import *

#### exec(open(r'C:\Python B10\file_handling_practice\Django_Projects\final_project\app\db.shell.py').read())  #we have paste it cmd 

# CRUD OPERTAION
# READ
# all_emps = Employee.objects.all()
# print(all_emps)
# # for emp in all_emps:
# #     print(emp)



# emp = Employee.objects.get(id = 10)
# emp = Employee.objects.filter(first_name__startswith = "E")
# print(emp)

# CREATE

# emp = Employee(first_name="Emp4", last_name="ustname", email="emp4@gmail.com", mob_no=54645154)
# emp.save()

#delete
# Employee.objects.get(id = 4).delete()

#UPDATE :- WE can update value of column
# emp = Employee.objects.get(id =2 )
# emp.first_name = "Employee2"
# emp.last_name = "Emplastname"
# emp.save() 

from datetime import datetime

# p3 = Person.objects.create(first_name="p3", last_name="pln3")

# p3 = Person.objects.get(id=4)

# Profile.objects.create(bio="student3",date_of_birth =datetime(1990, 1, 15), person_id=5)

# Person.objects.get(id = 5).delete()           #here we can delete the person profile


# -------------------------------------------------------------------------------------
# p1 = Person.objects.get(id=2)
# p3 = Person.objects.create(first_name="p3", last_name="pln3")
# p3


"""we are fetching here person to address"""
# for fetching Address for id 2               
# p1 = Person.objects.get(id=2)
# print(p1.address_set.all())                  #he khali cmd mdhe print krun det simply id 2 che sgle record

"""we are fetching address to person"""
# adr1 = Address.objects.get(id=2)             # he same khali cmd mdhe print krt aani id mapped jycha sobat asel tech print krt
# print(adr1.person)

# here we create the objects for address table
# Address.objects.create(street="SS Road", city="Arvi", state="MH",postal_code=442201, person=p1)
# Address.objects.create(street="aS Road", city="qrvi", state="MH",postal_code=432201, person=p1)

# Address.objects.create(street="wakad road", city="Pune", state="MH",postal_code=411057, person_id=p3.id)

# ------------------------------------------------------------------------------------------------------

# Many to many relationship
# Multiple records in a table are associated with multiple records in another table.

# c180 = CarModel.objects.create(name="C180")
# c200 = CarModel.objects.create(name="C200")
# print(CarModel.objects.all())


# gas = FuelType.objects.create(name="Gas")
# diesel = FuelType.objects.create(name="Diesel")
# hybrid = FuelType.objects.create(name="Hybrid")
# print(FuelType.objects.all())


# make relation with tables in M2M relationship
c180 = CarModel.objects.get(name = "C180")            #carmodelobject
# print(c180)

c200 = CarModel.objects.get(name = "C200")

# for fueltype



gas = FuelType.objects.get(name = "Gas")          #fueltypeobject
# print(gas)

# relation with tables in M2M relationship

"""here we make association table relation"""

# c180.fueltype.add(gas)            #carmodelobject.fueltype.add(fueltypeobject)

# diesel = FuelType.objects.get(name = "Diesel")  

# c180.fueltype.add(diesel)            #carmodelobject.fueltype.add(fueltypeobject)
# print(c180.fueltype.all())

"""make relation with another carmodel"""
c200 = CarModel.objects.get(name = "C200")
f1 = FuelType.objects.get(name = "Gas")  
f2 = FuelType.objects.get(name = "Diesel")  
f3 = FuelType.objects.get(name = "Hybrid")  
f4 = FuelType.objects.get(name = "Bio Diesel")  

#sgle add krysathi instance bnvle ahet
c200.fueltype.add(f1,f2,f3)
# print(c200.fueltype.all())

# c200.fueltype.add(c200)     #TypeError: 'FuelType' instance expected, got <CarModel: C200>

"""Create and add a FuelType to a CarModel in one step using create():""" 
# c200.fueltype.create(name="Bio Diesel")

# print(c200.fueltype.all()) 
# print(c200.fueltype.all())
# print(FuelType.objects.all())
# """Associate the FuelType with a CarModel"""
# print(f1.carmodel_set.all())

# print(FuelType.objects.get(name = "Bio Diesel").carmodel_set.all())

# FuelType.objects.get(name="Gas").carmodel_set.all()

"""after adding related_name='models' at Class CarModel"""
# print(f1.models.all())      #substitute method for that

# print(CarModel.objects.filter(fueltype__name__startswith="G"))
# print(FuelType.objects.filter(models__name__startswith="C"))

# print(c200.fueltype.all())
# print(c200.fueltype.remove(f3))
print(c200.fueltype.all())