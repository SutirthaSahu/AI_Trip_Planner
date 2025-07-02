import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper

load_dotenv()

@tool
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


def add(a:int, b:int) -> int:
    """
    Multiply 2 integers 

    Args:
        a (int) : First integer
        b (int) : Second integer
    
    Returns:
        int : The summation of a and b
    """

    return a + b

@tool
def currency_converter(from_curr: str, to_curr: str, value: float) -> float:
    os.environ["ALPHAVANTAGE_API_KEY"] = os.getenv('ALPHAVANTAGE_API_KEY')
    alpha_vantage = AlphaVantageAPIWrapper()
    response = alpha_vantage._get_exchange_rate(from_curr, to_curr)
    exchange_rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
    return value * float(exchange_rate)