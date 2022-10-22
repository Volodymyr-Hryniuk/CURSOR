# 1. Створіть клас Vehicle з атрибутами екземпляра max_speed і mileage та методами
# increase_speed, break_speed, mileage_info

print("#1")


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self):
        print(f"The speed can be increased to: {self.max_speed} Km/h.")

    def break_speed(self):
        pass

    def mileage_info(self):
        print(f"Vehicle have mileage: {self.mileage} Km.")


car = Vehicle(max_speed=160, mileage=150000)

car.mileage_info()
car.increase_speed()
car.break_speed()


# 2. Створіть дочірній клас Bus, який успадкує всі змінні та методи класу Vehicle
# і матиме власний метод seating_capacity

print("\n#2")


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seats_on_the_bus):
        super().__init__(max_speed, mileage)
        self.seats_on_the_bus = seats_on_the_bus

    def seating_capacity(self):
        print(f"Bus have capacity {self.seats_on_the_bus} people.")


bus = Bus(max_speed=120, mileage=560000, seats_on_the_bus=45)

bus.mileage_info()
bus.seating_capacity()
bus.increase_speed()

# 3. Визначте, від якого класу успадковується клас Bus (перевірте issubclass)

print("\n#3")

print("Bus is subclass Vehicle?", issubclass(Bus, Vehicle))
# print(Bus.__mro__)

# 4. Створіть екземпляр Bus під назвою school_bus і визначте, чи є school_bus об'єктом класу Vehicle/Bus

print("\n#4")

school_bus = Bus(max_speed=100, mileage=100000, seats_on_the_bus=50)

print("School bus is object Bus?", isinstance(school_bus, Bus))
print("School bus is object Vehicle?", isinstance(school_bus, Vehicle))

# 5. Створіть новий клас School з атрибутами екземпляра get_school_id і number_of_students та методами
# school_address, main_subject

print("\n#5")


class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def school_address(self):
        print("This school has an id", self.get_school_id)

    def main_subject(self):
        print(f"This year, {self.number_of_students} students chose mathematics as the main subject.")


social_school = School(get_school_id="IG315", number_of_students=156)

social_school.school_address()
social_school.main_subject()

# 6*. Створіть новий клас SchoolBus, який успадкує всі методи від School і Bus і матиме власний - bus_school_color

print("\n#6")


class SchoolBus(School, Bus):
    def __init__(self, get_school_id, number_of_students, max_speed, mileage, seats_on_the_bus, bus_color):
        self.bus_color = bus_color
        super().__init__(get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seats_on_the_bus)

    def bus_school_color(self):
        print("Bus color is:", self.bus_color)


bus_school = SchoolBus(get_school_id='123', number_of_students=15,
                       max_speed=100, mileage=9000, seats_on_the_bus=60,
                       bus_color="yellow")

bus_school.bus_school_color()
bus_school.mileage_info()
bus_school.increase_speed()
bus_school.seating_capacity()
bus_school.school_address()
bus_school.main_subject()

# 7. Поліморфізм: Створіть два класи: Bear, Wolf. Обидва вони повинні мати метод eat. Створіть два екземпляри:
# від Ведмідь і від Вовк, створіть із нього кортеж і використовуючи спільну змінну, викличте метод eat.

print("\n#7")


class Bear:
    def __init__(self, eat_for_bear):
        self.eat_for_bear = eat_for_bear

    def eat(self):
        print('Bear today eated:', self.eat_for_bear)


class Wolf:
    def __init__(self, eat_for_wolf):
        self.eat_for_wolf = eat_for_wolf

    def eat(self):
        print('Wolf today eated:', self.eat_for_wolf)


for_wolf = Wolf(eat_for_wolf='rabbit meat')
for_bear = Bear(eat_for_bear='fish')

animals = (for_bear, for_wolf)
# print(type(animals))
for food in animals:
    food.eat()


# 8*. Створіть клас City з атрибутами екземпляра name i population, сторіть новий екземпляр цього класу,
# лише коли population > 1500, інакше повертається повідомлення: "Your city is too small".
# Підказка: використовуєте для цього завдання, магічні методи.

print("\n#8")


class City:
    city = []

    def __new__(cls, name, population):
        cls.city = [name, population]
        if cls.city[1] < 1500:
            return print(f"Your city is too small")
        else:
            return print(f'The city of {cls.city[0]} has a population of {cls.city[1]} people')

    def __init__(self, name, population):
        self.name = name
        self.population = population


Kiyv = City('Kiyv', 2950702)
Boryspil = City('Boryspil', 64117)
Gorbovichi = City('Gorbovichi', 267)
Kharkiv = City('Kharkiv', 1421125)
Zhitomir = City('Zhitomir', 261358)
