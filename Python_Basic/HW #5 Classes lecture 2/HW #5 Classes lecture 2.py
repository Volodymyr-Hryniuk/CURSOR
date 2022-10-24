import dataclasses

# 1.
print("#1")


class Laptop:
    """
    Make the class with composition.
    """

    def __init__(self):
        part = Battery('Battery is a part of laptop')
        self.laptop = part.device


class Battery:
    """
    Make the class with composition.
    """
    def __init__(self, device):
        self.device = device


battery = Laptop()
print(battery.laptop)

cell = Battery(device='Six cell')
print(cell.device)

# 2.
print("\n#2")


class Guitar:
    """
    Make the class with aggregation
    """
    def __init__(self, string):
        self.string = string


class GuitarString:
    """
    Make the class with aggregation
    """
    def __init__(self, string_type):
        self.string_type = string_type


guitar = GuitarString(string_type='metal string')
fender = Guitar(guitar)

guitar_six_string = Guitar(string='Six string')
print(guitar_six_string.string)

metal_string_guitar = GuitarString(string_type='Metal string')
print(metal_string_guitar.string_type)

# 3
print("\n#3")


class Calc:
    """
    Створіть клас з одним методом "add_nums" та 3 атрибутами, який повертає суму цих атрибутів.
    """
    def __init__(self, atr_1, atr_2, atr_3):
        self.atr_1 = atr_1
        self.atr_2 = atr_2
        self.atr_3 = atr_3

    def add_nums(self):
        sum_atr = sum([self.atr_1, self.atr_2, self.atr_3])
        return sum_atr


nums = Calc(54, 33, 22)
print(nums.add_nums())

# 4*.
print("\n#4")


class Pasta:
    """
    Створіть клас, який приймає 1 атрибут при ініціалізації - ingredients і визначає інгридієнти атрибута екземпляра.
    Він повинен мати 2 методи:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """


# 5*.
print("\n#5")


class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """


# 6.
print("\n#6")


@dataclasses.dataclass
class AddressBookDataClass:
    """
    Create dataclass with 7 fields - key (int), name (str), phone_number (str),
                                     address (str), email (str), birthday (str), age (int)
    """
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


address_book = AddressBookDataClass(1, 'ivan', '095xxxxxxx', 'Ozerna str.', 'xxx@ukr.net', '6 December', 23)
address_book_1 = AddressBookDataClass(1, 'ihor', '096xxxxxxx', 'Bolotna str.', '1xx@ukr.net', '25 November', 25)

print(address_book)
print(address_book_1)

# 7. Create the same class (6) but using NamedTuple
print("\n#7")


# 8.
print("\n#8")


class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    Expected result by printing instance of
    AddressBook: AddressBook(key='', name='', phone_number='', address='', email='', birthday= '', age='')
    """


# 9.
print("\n#9")


class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"


# 10.
print("\n#10")


class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name
