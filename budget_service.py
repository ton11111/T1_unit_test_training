from typing import List
from dataclasses import dataclass
import datetime
import calendar


@dataclass
class Budget:
    year_month: str
    amount: int


class BudgetRepo:

    def get_all(self) -> List[Budget]:
        return NotImplementedError


class BudgetService:

    # def has_data(self, budgets, start_dt, end_dt):
    #     if budgets:
    #         return True
    #     return False

    def is_whole_month(self, start_dt: datetime.datetime, end_dt: datetime.datetime) -> bool:
        if start_dt.year == end_dt.year and start_dt.month == end_dt.month:
            month_days = calendar.monthrange(start_dt.year, start_dt.month)[1]
            return (end_dt - start_dt).days + 1 == month_days
        return False

    def is_valid(self, start_dt, end_dt):
        return end_dt > start_dt

    def query(self, start_dt, end_dt) -> float:
        if self.is_valid(start_dt, end_dt):
            return 0.0

        budget_repo = BudgetRepo()
        budgets = budget_repo.get_all()

        budgets
