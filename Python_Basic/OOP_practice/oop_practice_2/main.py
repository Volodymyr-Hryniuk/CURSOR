from datetime import date
from decimal import Decimal
from classes import Employee

john = Employee(name="John", start=date(2022, 10, 5), rate=Decimal("11"), taxes=10)


# john.update_rate(Decimal('10'))
# print(john.how_long())
# print('\n')

Employee.show_line()
Employee.show_row(john)
Employee.show_line()
