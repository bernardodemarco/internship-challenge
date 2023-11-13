import math


def is_prime(num: int) -> bool:
    """
    Determine if the given number is prime using a linear approach.

    Args:
        num (int): the number to evaluate.

    Returns:
        bool: flag indicating whether the number is prime or not.
    """
    if num < 2 or (num > 2 and num % 2 == 0):
        return False
    
    if num == 2:
        return True
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
        
    return True
