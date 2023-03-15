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

    def is_cross_month(self, start_dt, end_dt):
        if start_dt.year != end_dt.year or start_dt.month != end_dt.month:
            return True
        return False

    def get_budget(self, start_dt, budgets):
        for b in budgets:
            if start_dt.strftime("%Y%m") == b.year_month:
                return (b.amount or 0)
        return 0

    def query(self, start_dt, end_dt) -> float:
        budget_repo = BudgetRepo()
        budgets = budget_repo.get_all()
        if self.is_valid(start_dt, end_dt):
            if self.is_cross_month(start_dt, end_dt):
                print()
            else:
                if self.is_whole_month(start_dt, end_dt):
                   return self.get_budget(start_dt, budgets)
                else:
                    partial_days = (end_dt - start_dt).days + 1
                    month_days = calendar.monthrange(start_dt.year, start_dt.month)[1]
                    return self.get_budget(start_dt, budgets) * partial_days / month_days
        return 0.0


