"""Tests for classes exercises"""
import math
import unittest

from classes import BankAccount, Point, MinimumBalanceAccount, Person, Circle


class BankAccountTests(unittest.TestCase):

    """Tests for BankAccount."""

    def test_new_account_balance_default(self):
        account = BankAccount()
        self.assertEqual(account.balance, 0)

    def test_opening_balance(self):
        account = BankAccount(balance=100)
        self.assertEqual(account.balance, 100)

    def test_deposit(self):
        account = BankAccount()
        account.deposit(100)
        self.assertEqual(account.balance, 100)

    def test_withdraw(self):
        account = BankAccount(balance=100)
        account.withdraw(40)
        self.assertEqual(account.balance, 60)

    def test_str(self):
        account = BankAccount()
        self.assertEqual(str(account), 'Account with balance of $0')
        account.deposit(200)
        self.assertEqual(str(account), 'Account with balance of $200')

    def test_repr(self):
        account = BankAccount()
        self.assertEqual(repr(account), 'BankAccount(balance=0)')
        account.deposit(200)
        self.assertEqual(repr(account), 'BankAccount(balance=200)')

    # Transfers
    @unittest.expectedFailure
    def test_transfer(self):
        mary_account = BankAccount(balance=100)
        dana_account = BankAccount(balance=0)
        mary_account.transfer(dana_account, 20)
        self.assertEqual(mary_account.balance, 80)
        self.assertEqual(dana_account.balance, 20)

    # Transactions
    @unittest.expectedFailure
    def test_transactions_open(self):
        expected_transactions = [
            ('OPEN', 100, 100),
        ]
        account = BankAccount(balance=100)
        self.assertEqual(account.transactions, expected_transactions)

    @unittest.expectedFailure
    def test_transactions_deposit(self):
        expected_transactions = [
            ('OPEN', 0, 0),
            ('DEPOSIT', 100, 100),
        ]
        account = BankAccount()
        account.deposit(100)
        self.assertEqual(account.transactions, expected_transactions)

    @unittest.expectedFailure
    def test_transactions_withdraw(self):
        expected_transactions = [
            ('OPEN', 100, 100),
            ('WITHDRAWAL', -40, 60),
        ]
        account = BankAccount(balance=100)
        account.withdraw(40)
        self.assertEqual(account.transactions, expected_transactions)

    @unittest.expectedFailure
    def test_transactions_scenario(self):
        expected_transactions = [
            ('OPEN', 0, 0),
            ('DEPOSIT', 100, 100),
            ('WITHDRAWAL', -40, 60),
            ('DEPOSIT', 95, 155),
        ]
        account = BankAccount()
        account.deposit(100)
        account.withdraw(40)
        account.deposit(95)
        self.assertEqual(account.transactions, expected_transactions)

    # Record Transactions
    @unittest.expectedFailure
    def test_transactions_with_transfer(self):
        mary_transactions = [
            ('OPEN', 100, 100),
            ('WITHDRAWAL', -20, 80),
        ]
        dana_transactions = [
            ('OPEN', 0, 0),
            ('DEPOSIT', 20, 20),
        ]
        mary_account = BankAccount(balance=100)
        dana_account = BankAccount(balance=0)
        mary_account.transfer(dana_account, 20)
        self.assertEqual(mary_account.transactions, mary_transactions)
        self.assertEqual(dana_account.transactions, dana_transactions)


class PointTests(unittest.TestCase):

    """Tests for Point."""

    def test_attributes(self):
        point = Point(1, 2, 3)
        self.assertEqual((point.x, point.y, point.z), (1, 2, 3))

    def test_str(self):
        point = Point(1, 2, 3)
        self.assertEqual(str(point), 'Point(1, 2, 3)')

    # This is commented out for testing the Points exercise
    # Uncomment the following line when testing Pythonic Points exercise
    # @unittest.expectedFailure
    def test_scale(self):
        p1 = Point(1, 2, 3)
        p2 = p1.scale(2)
        self.assertEqual(str(p2), 'Point(2, 4, 6)')

    # This is commented out for testing the Points exercise
    # Uncomment the following line when testing Pythonic Points exercise
    # @unittest.expectedFailure
    def test_shift(self):
        p1 = Point(1, 2, 3)
        p2 = Point(4, 5, 6)
        p3 = p2.shift(p1)
        self.assertEqual(str(p3), 'Point(5, 7, 9)')

    def test_distance(self):
        p1 = Point(1, 2, 3)
        p2 = Point(4, 5, 6)
        self.assertEqual(p1.distance(p2), 5.196152422706632)

    # This failure is expected when testing the Points exercise
    # Comment the following line when testing Pythonic Points exercise
    @unittest.expectedFailure
    def test_add(self):
        p1 = Point(1, 2, 3)
        p2 = Point(4, 5, 6)
        p3 = p1 + p2
        self.assertEqual(str(p3), 'Point(5, 7, 9)')

    # This failure is expected when testing the Points exercise
    # Comment the following line when testing Pythonic Points exercise
    @unittest.expectedFailure
    def test_multiply(self):
        p1 = Point(1, 2, 3)
        p2 = p1 * 2
        self.assertEqual(str(p2), 'Point(2, 4, 6)')
        p3 = 2 * p1
        self.assertEqual(str(p3), 'Point(2, 4, 6)')

    # This failure is expected when testing the Points exercise
    # Comment the following line when testing Pythonic Points exercise
    @unittest.expectedFailure
    def test_equality(self):
        p1 = Point(1, 2, 3)
        p2 = Point(4, 5, 6)
        p3 = Point(1, 2, 3)
        self.assertEqual(p1, p3)
        self.assertNotEqual(p1, p2)
        self.assertTrue(p1 == p3)
        self.assertFalse(p1 != p3)
        self.assertFalse(p1 == p2)
        self.assertTrue(p1 != p2)
        self.assertFalse(p1 != p3)


class MinimumBalanceAccountTests(unittest.TestCase):

    """Tests for MinimumBalanceAccount."""

    def test_withdraw_from_new_account(self):
        account = MinimumBalanceAccount()
        with self.assertRaises(ValueError):
            account.withdraw(1)

    def test_exception_message(self):
        account = MinimumBalanceAccount()
        with self.assertRaises(ValueError) as cm:
            account.withdraw(1000)
        self.assertEqual(str(cm.exception), "Balance cannot be less than $0")

    def test_withdraw_above_zero(self):
        account = MinimumBalanceAccount()
        account.deposit(100)
        account.withdraw(99)
        self.assertEqual(account.balance, 1)

    def test_withdraw_to_exactly_zero(self):
        account = MinimumBalanceAccount()
        account.deposit(100)
        account.withdraw(100)
        self.assertEqual(account.balance, 0)

    def test_withdraw_to_below_zero(self):
        account = MinimumBalanceAccount()
        account.deposit(100)
        with self.assertRaises(ValueError):
            account.withdraw(101)

    def test_repr(self):
        account = MinimumBalanceAccount()
        self.assertEqual(repr(account), 'MinimumBalanceAccount(balance=0)')


class PersonTests(unittest.TestCase):

    """Tests for Person."""

    def test_construct(self):
        Person("Trey", "Hunner")

    def test_first_and_last_name_attributes(self):
        trey = Person("Trey", "Hunner")
        self.assertEqual(trey.first_name, "Trey")
        self.assertEqual(trey.last_name, "Hunner")

    def test_name_attribute(self):
        trey = Person("Trey", "Hunner")
        self.assertEqual(trey.name, "Trey Hunner")

    def test_change_names(self):
        trey = Person("Trey", "Hunner")
        trey.last_name = "Smith"
        self.assertEqual(trey.name, "Trey Smith")
        trey.first_name = "John"
        self.assertEqual(trey.name, "John Smith")


class CircleTests(unittest.TestCase):

    """Tests for Circle."""

    def test_radius(self):
        circle = Circle(5)
        self.assertEqual(circle.radius, 5)

    def test_default_radius(self):
        circle = Circle()
        self.assertEqual(circle.radius, 1)

    def test_diameter_changes(self):
        circle = Circle(2)
        self.assertEqual(circle.diameter, 4)
        circle.radius = 3
        self.assertEqual(circle.diameter, 6)

    def test_set_diameter(self):
        circle = Circle(2)
        self.assertEqual(circle.diameter, 4)
        circle.diameter = 3
        self.assertEqual(circle.radius, 1.5)

    def test_area(self):
        circle = Circle(2)
        self.assertEqual(circle.area, math.pi * 4)

    # Log Radius Changes
    @unittest.expectedFailure
    def test_radius_changes_logged(self):
        circle = Circle(2)
        self.assertEqual(circle.radius_changes, [2])
        circle.radius = 3
        self.assertEqual(circle.radius_changes, [2, 3])
        circle.diameter = 3
        self.assertEqual(circle.radius_changes, [2, 3, 1.5])

    # Set Radius Error
    @unittest.expectedFailure
    def test_no_negative_radius(self):
        circle = Circle(2)
        with self.assertRaises(ValueError) as context:
            circle.radius = -10
        self.assertEqual(str(context.exception), "Radius cannot be negative")

    # Comparable Circle
    @unittest.expectedFailure
    def test_equality(self):
        circleA = Circle(2)
        circleB = Circle(2)
        circleC = Circle(1)
        self.assertTrue(circleA == circleB)
        self.assertTrue(circleB != circleC != circleA)
        self.assertFalse(circleA != circleB)
        self.assertFalse(circleA == circleC)
        self.assertFalse(circleB == circleC)
        circleC.radius = 2
        self.assertTrue(circleA == circleB == circleC)
        self.assertFalse(circleB != circleC)
        self.assertFalse(circleA != circleC)

    # Comparable Circle
    @unittest.expectedFailure
    def test_comparability(self):
        circleA = Circle(1)
        circleB = Circle(2)
        circleC = Circle(3)
        self.assertTrue(circleA < circleB < circleC)
        self.assertTrue(circleA <= circleB <= circleC)
        self.assertFalse(circleB < circleA)
        self.assertFalse(circleC < circleB)
        self.assertTrue(circleC > circleB > circleA)
        self.assertTrue(circleC >= circleB >= circleA)
        self.assertFalse(circleA > circleB)
        self.assertFalse(circleB > circleC)


if __name__ == "__main__":
    unittest.main()
