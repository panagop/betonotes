"""Utility functions for betonotes."""


def greet(name: str) -> str:
    """
    Return a greeting message.
    
    Args:
        name: The name to greet
        
    Returns:
        A greeting string
    """
    return f"Hello, {name}! Welcome to betonotes."


def calculate_sum(numbers: list[float]) -> float:
    """
    Calculate the sum of a list of numbers.
    
    Args:
        numbers: List of numbers to sum
        
    Returns:
        The sum of all numbers
    """
    return sum(numbers)
