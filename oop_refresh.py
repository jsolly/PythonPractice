class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("delete name")
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.raise_amt * self.pay)

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    def __repr__(self):
        return f"Employee('{self.first}, {self.last}, {self.pay})"

    def __str__(self):
        return f"{self.fullname}, {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay)
        self.programming_language = programming_language


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if not employees:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for emp in self.employees:
            print("-->", emp.fullname())
