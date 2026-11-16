class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class EmployeeIterator:
    def __init__(self, employees):
        self._employees = employees
        self._index = 0

    def has_next(self):
        return self._index < len(self._employees)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.has_next():
            raise StopIteration

        employee = self._employees[self._index]
        self._index += 1
        return employee


class Company:
    def __init__(self, employees):
        self._employees = employees

    def __iter__(self):
        return EmployeeIterator(self._employees)


employees = [
    Employee("Alice", 50000),
    Employee("Bob", 60000),
    Employee("Charlie", 70000),
]

company = Company(employees)

total_salary = 0
for employee in company:
    print(f"{employee.name}: {employee.salary}")
    total_salary += employee.salary

print(f"Total salary: {total_salary}")
