class Calculator:

    @staticmethod
    def multiply(a:int, b:int) -> int:
        """
        Multiply 2 integers 

        Args:
            a (int) : First integer
            b (int) : Second integer
        
        Returns:
            int : The product of a and b
        """

        return a * b
    
    @staticmethod
    def calculate_total( *x:float) -> float:
        """
        Calculate the sum of the list of the numbers 

        Args:
            x (list) : List of floating numbers
        
        Returns:
            float : The sum of the list of numbers
        """

        return sum(x)
    

    @staticmethod
    def calculate_daily_budget(total: float, days:int) -> float:
        """
        Calculate the daily budget

        Args:
            total (float) : Total Cost
            days (int) : Total number of days

        Returns:
            float : Expense for a single day
        """

        return total/days if days > 0 else 0

