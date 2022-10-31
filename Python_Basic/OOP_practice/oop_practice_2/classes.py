from datetime import date
from decimal import Decimal

from decorator import timer


class Employee:

    ROW_FORMAT = "| {:<30} | {:<10} | {:<10} | {:<10} |"
    ROW_LENGTH = 73

    def __init__(self, name: str, start: date, rate: Decimal, taxes: int, end: date = date.today()):
        self.validation(name=name, start=start, end=end, rate=rate, taxes=taxes)
        self.name = name
        self._start = start
        self._end = end
        self._rate = rate
        self._taxes = taxes
        self._balance = self._recalculate_balance()

    @staticmethod
    def validation(name: str, start: date, rate: Decimal, taxes: int, end: date):
        if not end > start:
            raise ValueError("Start date can't be more then today")
        if not Decimal("100") > rate > Decimal("10"):
            raise ValueError("Rate must be between 10 and 100")
        if not 99 >= taxes > 1:
            raise ValueError("Taxes must be between 1 and 99")
        if not 20 >= len(name) > 2:
            raise ValueError("Name must be from 2 to 20 characters")

    def days(self):
        return (self._end - self._start).days

    def how_long(self):
        return f"{self.name} works {self.days()} day(s)"

    def _recalculate_balance(self):
        self._balance = self._rate * self.days()
        return self._balance

    @timer
    def update_rate(self, rate):
        self._rate = rate
        self._balance = self._recalculate_balance()
        return self._rate

    @property
    def rate(self):
        return self._rate

    @classmethod
    def show_line(cls):
        print(cls.ROW_LENGTH * "-")

    @staticmethod
    def show_row(cls):
        _name = cls.how_long()
        _balance = cls._balance
        _taxes_pay = cls._taxes * cls.days()
        _salary = cls._balance - _taxes_pay
        date = [_name, _balance, _taxes_pay, _salary]
        print(cls.ROW_FORMAT.format(*date))
