class Livingthing:
    def __init__(self, name,color):
        self.name=name
        self.color=color
    def growth(self):
        return("I can grow")

    def get_offsprings(self):
        return("Every livingthing can have offsprings")

class Animal(Livingthing):
    def __init__(self, name, color, age):
        super().__init__(name, color)
        self.__age=8
    def get_offsprings(self, method, gestation_period):
        return ("{} gets offsprings through {} after {}".format(self.name, method, gestation_period))

class Bird(Livingthing):
    def __init__(self, name, color, age) -> None:
        super().__init__(name, color)
        self.__age=3
    def getAge(self):
        return self.__age
    def get_offsprings(self, method, gestation_period):
        return ("{} gets offsprings through {} and sitting on them for {}".format(self.name, method, gestation_period))

lion=Animal("Kitty", "brown", "8")
print(lion.get_offsprings("fertilization", "110 days"))
print(lion.age)
my_bird=Bird("Timmy", "black","21 days" )
print(my_bird.get_offsprings("laying eggs", "21 days"))
print(lion.growth())
print(my_bird.growth())
print(my_bird.getAge())
print(my_bird.__age)

    