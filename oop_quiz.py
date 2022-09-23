"""1. create a credit card class with the following attributes:
 card number, expiration date, and security code. 
 Create a method that will print out the card number, 
 expiration date, and security code. Create an instance of
  the class and call the method."""

class Credit_Card:
    def __init__(self, card_number, expiration_date, security_code):
        self.card_number=card_number
        self.expiration_date=expiration_date
        self.security_code=security_code

    def credit_card_details(self, card_number, expiration_date, security_code):
        print("card_number:{}\nexpiration_date:{}\nsecurity_code:{}". format(card_number, expiration_date, security_code))
      
my_credit_card=Credit_Card("101", "16/10/2030", "344558")
my_credit_card.credit_card_details("101", "16/10/2030", "344558")

"""2. create Animal class and Dog class. Make the Dog class inherit from 
the Animal class. Add a bark method to the Dog class. Create an instance of 
the Dog class and call the bark method."""

class Animal:
    def __init__(self, name,color):
        self.name=name
        self.color=color
class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)
    def bark(self, name):
        print("I {} can bark". format(self.name))
my_dog=Dog("Rafa", "white")
my_dog.bark("Rafa")

"""5. create a class called Person. The class should have the following attributes: 
name, age, and address. The class should have the following methods: eat, 
sleep, and work. The eat method should print out the name of the 
person and the word "is eating". The sleep method should print out 
the name of the person and the word "is sleeping". The work method should 
print out the name of the person and the word "is working"."""

class Person:
    def __init__(self, name, age, address):
        self.name=name
        self.age=age
        self.adress=address
    def eat(self):
        print("{} is eating".format(self.name))
    def sleep(self):
        print("{} is sleeping".format(self.name))
    def work(self):
        print("{} working".format(self.name))
me=Person("Elsa", "20", "Namasuba")
me.eat()
me.sleep()
me.work()

"""6. create a class called Employee. The class should have the following attributes:
name, age, and salary. The class should have the following methods:
eat, sleep, and work. The eat method should print out the name of the person 
and the word "is eating". The sleep method should print out the name 
of the person and the word "is sleeping". The work method should print
out the name of the person and the word "is working". Create a subclass
of Employee called Programmer. The Programmer class should have the following
attributes: name, age, salary, and programming language. The Programmer class 
should have the following methods: eat, sleep, work, and code. The code method
should print out the name of the person and the word "is coding in" and the 
programming language. Create an instance of the Programmer class and call all 
the methods."""
class Employee:
    def __init__(self, name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary
    def eat(self):
        print("{} is eating".format(self.name))
    def sleep(self):
        print("{} is sleeping".format(self.name))
    def work(self):
        print("{} is working".format(self.name))
class Programmer(Employee):
    def __init__(self, name, age, salary, programmig_language):
        super().__init__(name, age, salary)
        self.programming_language=programmig_language
    def code(self):
        print("{} is coding in {}".format(self.name, self.programming_language))
my_dog=Programmer("Kelly", "32", "10million", "python")
my_dog.eat()
my_dog.sleep()
my_dog.work()
my_dog.code()

"""7. create a class called Vehicle. The class should have the following attributes:
make, model, and year. The class should have the following methods:
start, stop, and drive. The start method should print out the make, model,
and year of the vehicle and the word "is starting". The stop method should 
print out the make, model, and year of the vehicle and the word "is stopping".
The drive method should print out the make, model, and year of the vehicle and
the word "is driving". Create a subclass of Vehicle called Car. The Car class 
should have the following attributes: make, model, year, and color. The Car 
class should have the following methods: start, stop, drive, and park. 
The park method should print out the make, model, year, and color of the car 
and the word "is parking". Create an instance of the Car class and call all the
methods."""

class Animal:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        print("{} {} {} is starting".format(self.make, self.model, self.year))
    def stop(self):
        print("{} {} {} is stopping".format(self.make, self.model, self.year))
    def drive(self):
        print("{} {} {} is driving".format(self.make, self.model, self.year))
class Car(Animal):
    def __init__(self,make, model, year, color ):
        super().__init__(make, model, year)
        self.color=color
    def park(self):
        print("{} {} {} {} is parking".format(self.color, self.make, self.model, self.year))
my_dog=Car("Mercedes-Benz", "A-class","2022", "Black")
my_dog.start()
my_dog.stop()
my_dog.drive()
my_dog.park()

"""8. create a class called Animal. The class should have the following attributes: 
name, color, and age. The class should have the following methods: eat, sleep, and 
make_sound. The eat method should print out the name of the animal and the word 
"is eating". The sleep method should print out the name of the animal and the 
word "is sleeping". The make_sound method should print out the name of the 
animal and the word "is making a sound". Create a subclass of Animal called Dog. 
The Dog class should have the following attributes: name, color, age, and breed. 
The Dog class should have the following methods: eat, sleep, make_sound, and bark. 
The bark method should print out the name of the dog and the word "is barking". 
Create an instance of the Dog class and call all the methods."""

class Animal:
    def __init__(self, name, color, age):
        self.name=name
        self.color=color
        self.age=age
    def eat(self):
        print("{} is eating".format(self.name))
    def sleep(self):
        print("{} is sleeping".format(self.name))
    def make_sound(self):
        print("{} is making a sound".format(self.name))
class Dog(Animal):
    def __init__(self, name, color, age,breed):
        super().__init__(name, color, age)
        self.breed=breed
    def bark(self):
        print("{} is barking".format(self.name ))
my_dog=Dog("Zinia", "grey", "3", "bulldog")
my_dog.eat()
my_dog.sleep()
my_dog.make_sound()
my_dog.bark()

"""9. create a class of your choice. It should have at least 3 attributes and 
3 methods where one of the methods is a static method. Implement polymorphism, 
encapsulation, and inheritance"""
from math import pow,pi
class Shape:
    def __init__(self, name):
        self.name=name
    def area(self):
        return 0
    @staticmethod
    def volume(self):
        return 0
class Cube(Shape):
    def __init__(self, name, length_of_sides, color):
        self.__color="blue"
        super().__init__(name)
        self.length_of_sides=length_of_sides
    def getColor(self):
        return(self.__color)
    #@staticmethod
    def volume(self,length_of_sides):
        print("volume of the cube is {}".format(pow(self.length_of_sides, 3)))
class Cylinder(Shape):
    def __init__(self, name, radius, height):
        super().__init__(name)
        self.radius=radius
        self.height=height
    #@staticmethod
    def volume(self,radius,height):
        print("The volume of the cylinder is {}".format(pi*pow(self.radius, 2)* self.height))
Cylinder.volume(2, 6)
Cube.volume(6)
my_shape=Cube("cube",6,"blue")
print(my_shape.getColor)



        


