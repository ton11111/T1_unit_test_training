import datetime
import unittest
from unittest.mock import patch

from budget_service import BudgetService, Budget


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.budgetService = BudgetService()
        get_all_patcher = patch("budget_service.BudgetRepo.get_all")
        self.fake_get_all_patcher = get_all_patcher.start()

    def give_date(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def test_budget_is_invalid(self):
        assert self.budgetService.is_valid(datetime.date(2023, 1, 2), datetime.date(2023, 1, 1)) is False

    def test_budget_is_whole_month(self):
        assert self.budgetService.is_whole_month(datetime.date(2023, 1, 1), datetime.date(2023, 1, 31)) is True

    def test_budget_is_empty_data(self):
        self.fake_get_all_patcher.return_value = []
        assert self.budgetService.query(datetime.date(2023, 1, 1), datetime.date(2023, 1, 31)) == 0

    def test_budget_is_valid(self):
        self.fake_get_all_patcher.return_value = [Budget('202301', 310)]
        assert self.budgetService.query(datetime.date(2023, 1, 1), datetime.date(2023, 1, 31)) == 310

if __name__ == '__main__':
    unittest.main()