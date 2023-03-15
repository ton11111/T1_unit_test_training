from typing import List
from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Budget:
    year_month: str
    amount: int


class BudgetRepo:

    def get_all(self) -> List[Budget]:
        return NotImplementedError


class BudgetService:

    def is_empty(self):


    def is_valid(self, start_dt, end_dt):
        if end_dt < start_dt:
            return False
        else:
            return True

    def query(self, start_dt, end_dt) -> float:
        if self.is_valid(start_dt, end_dt):
            return 0.0

