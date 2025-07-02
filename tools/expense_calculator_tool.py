import os
from dotenv import load_dotenv

from typing import List
from langchain.tools import tool

from utils.expense_calculator import Calculator

load_dotenv()

class CalculatorTool:

    def __init__(self):
        self.calculator = Calculator()
        self.calculator_tool_list = self._setup_tools()
    
    def _setup_tools(self):
        """ Setup all tools for the calculator tool"""

        @tool
        def estimate_total_hotel_cost(price_per_night: str, total_days:float) -> float:
            """ Calculate total hotel cost"""
            return self.calculator.multiply(price_per_night, total_days)
        
        @tool
        def calculate_total_expenses(*costs: float) -> float:
            """ Calculate total expenses of the trip"""
            return self.calculator.calculate_total(*costs)


        def calculate_daily_expense_budget(total_cost: float, days: int) -> float:
            """ Calculate daily expenses"""
            return self.calculator.calculate_daily_budget(total_cost, days)
        
        return [estimate_total_hotel_cost, calculate_total_expenses, calculate_daily_expense_budget]
