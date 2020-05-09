import unittest
from PythonPractice import oop_refresh


class TestEmployee(unittest.TestCase):

    def test_fullname(self):
        emp_1 = oop_refresh.Employee("john", "Solly", 100000)
        self.assertTrue(emp_1.fullname, "John Solly")

    def test_apply_raise(self):
        emp_1 = oop_refresh.Employee("john", "Solly", 100000)
        emp_1.apply_raise()
        self.assertTrue(emp_1.pay, 104000)

    def test_email(self):
        emp_1 = oop_refresh.Employee("John", "Solly", 100000)
        self.assertEqual(emp_1.email, "John.Solly@email.com")

    def test_str(self):
        emp_1 = oop_refresh.Employee("John", "Solly", 100000)
        self.assertEqual(str(emp_1), f"{emp_1.fullname}, {emp_1.email}")

    def test_repr(self):
        emp_1 = oop_refresh.Employee("John", "Solly", 100000)
        self.assertEqual(repr(emp_1), f"Employee('{emp_1.first}, {emp_1.last}, {emp_1.pay})")

    def test_add(self):
        emp_1 = oop_refresh.Employee("John", "Solly", 100000)
        emp_2 = oop_refresh.Employee("Martha", "Goldsmith", 90000)
        self.assertEqual(emp_1 + emp_2, 190000)

    def test_fullname_setter(self):
        emp_1 = oop_refresh.Employee("John", "Solly", 100000)
        emp_1.fullname = "Richard Solly"
        self.assertEqual(emp_1.fullname, "Richard Solly")

    def test_fullname_deleter(self):
        emp_1 = oop_refresh.Employee("John", "Solly", 100000)
        del emp_1.fullname
        self.assertEqual(emp_1.fullname, "None None")

    def test_len(self):
        emp_1 = oop_refresh.Employee("John", "Solly", 100000)
        self.assertTrue((len(emp_1), 9))


class TestDeveloper(unittest.TestCase):
    def test_developer(self):
        self.assertTrue(issubclass(oop_refresh.Developer, oop_refresh.Employee))


class TestManager(unittest.TestCase):
    def test_manager(self):
        self.assertTrue(issubclass(oop_refresh.Manager, oop_refresh.Employee))

    def test_add_emp(self):
        mgr_1 = oop_refresh.Manager("Chris", "Happy", 100000)
        emp_1 = oop_refresh.Employee("John", "Solly", 100000)
        mgr_1.add_emp(emp_1)
        self.assertTrue(emp_1 in mgr_1.employees)

    def test_remove_emp(self):
        emp_1 = oop_refresh.Employee("John", "Solly", 100000)
        mgr_1 = oop_refresh.Manager("Chris", "Happy", 100000,
                                    employees=[emp_1])
        mgr_1.remove_employee(emp_1)
        self.assertFalse(emp_1 in mgr_1.employees)
