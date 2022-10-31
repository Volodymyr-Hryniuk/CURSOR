# 1. Implement class iterator for Fibonacci numbers https://en.wikipedia.org/wiki/Fibonacci_number
# Iterator get numbers of first Fibonacci numbers
# Example:
# for i in FibonacciNumbers(10):
#     print(i)
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
print("#1")


class FibonacciNumbers:
    number = 0

    def __init__(self, count):
        self.count = count
        self.a, self.b = 0, 1

    def __getitem__(self, f_number):
        self.number += 1
        if self.number == self.count:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return self.b


for i in FibonacciNumbers(11):
    print(i)

# 2.* Implement generator for Fibonacci numbers
print("\n#2")


class FibonacciGenerator:
    def __init__(self, count):
        self.count = count
        self.current_number, self.next_number = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        self.count -= 1
        next_number = self.current_number + self.next_number
        self.current_number = self.next_number
        self.next_number = next_number

        return self.current_number


for i in FibonacciGenerator(10):
    print(i)

# 3. Write generator expression that returns square numbers of integers from 0 to 10
print("\n#3")

# 4. Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.
print("\n#4")

# 5. Create an abstract class for the Car with the next methods: drive, stop, open_door, close_door, turn_on_light,
# turn_off_light, enable_radio, disable_radio, where drive and stop will be predefined with some realization, all others
# should be abstract.
print("\n#5")
