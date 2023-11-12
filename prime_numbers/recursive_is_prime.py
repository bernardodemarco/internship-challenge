import math


def recursive_is_prime(num: int, divisor: int = 2) -> bool:
    """
    Determine if the given number is prime using a recursive approach.

    Args:
        num     (int): the number to evaluate.
        divisor (int, optional): the divisor used in the recursive calls. Defaults to 2.

    Returns:
        bool: flag indicating whether the number is prime or not.
    """
    if num < 2 or (num > 2 and num % 2 == 0):
        return False
    
    if num == 2 or divisor > math.sqrt(num):
        return True
    
    not_divisible = num % divisor != 0
    return not_divisible and recursive_is_prime(num, divisor + 1)
