from abc import abstractmethod, ABC

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
        self.current_number, self.next_number = 0, 1

    def __getitem__(self, number):
        self.number += 1
        if self.number == self.count:
            raise StopIteration
        self.current_number, self.next_number = self.next_number, self.current_number + self.next_number
        return self.next_number


for i in FibonacciNumbers(10):
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

print("\n#2 - Second Version")


class FibonacciGenerator:
    def __init__(self, count):
        self.count = count
        self.current_number, self.next_number = 0, 1

    def fibonacci_generator(self):
        while 0 < self.count:
            self.current_number, self.next_number = self.next_number, self.current_number + self.next_number
            yield self.next_number
            self.count -= 1


iteration = FibonacciGenerator(10)
for i in iteration.fibonacci_generator():
    print(i)

# 3. Write generator expression that returns square numbers of integers from 0 to 10
print("\n#3")


def square(count):
    for x in range(1, count):
        yield x**2


for i in square(10):
    print(i)

# 4. Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.

# print("\n#4")


class Laptop (ABC):

    @abstractmethod
    def screen(self):
        print('Hello World')

    @abstractmethod
    def keyboard(self):
        print('Input device')

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):

    def __init__(self):
        self.parameters = {}

    def screen(self):
        return 'Hello World'

    def keyboard(self):
        print('Input device')

    def touchpad(self):
        print('Touch input device')

    def webcam(self):
        print('Video recording Device')

    def ports(self):
        print('Devices are connected using ports')

    def dynamics(self):
        print('Sound output device')


# 5. Create an abstract class for the Car with the next methods: drive, stop, open_door, close_door, turn_on_light,
# turn_off_light, enable_radio, disable_radio, where drive and stop will be predefined with some realization, all others
# should be abstract.

# print("\n#5")


class Car (ABC):

    def drive(self):
        print('Drive')

    def stop(self):
        print('Stop')

    @abstractmethod
    def open_door(self):
        raise NotImplementedError

    @abstractmethod
    def close_door(self):
        raise NotImplementedError

    @abstractmethod
    def turn_on_light(self):
        raise NotImplementedError

    @abstractmethod
    def turn_off_light(self):
        raise NotImplementedError

    @abstractmethod
    def enable_radio(self):
        raise NotImplementedError

    @abstractmethod
    def disable_radio(self):
        raise NotImplementedError
