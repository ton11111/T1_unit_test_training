import datetime
import unittest

from budget_service import BudgetService


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.budgetService = BudgetService()

    def give_date(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def test_budget_is_invalid(self):
        assert self.budgetService.is_valid(datetime.date(2023, 1, 2), datetime.date(2023, 1, 1)) is False

    def test_budget_is_whole_month(self):
        assert self.budgetService.is_whole_month(datetime.date(2023, 1, 1), datetime.date(2023, 1, 31)) is True


if __name__ == '__main__':
    unittest.main()