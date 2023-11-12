def recursive_fib(position: int) -> int:
    """
    Calculate the Fibonacci value at the given position using a recursive approach.

    Args:
        position (int): the position in the Fibonacci sequence.

    Returns:
        int: the Fibonacci value at the given position
    """
    if position == 0:
        return 0
    
    if position == 1:
        return 1
    
    return recursive_fib(position - 1) + recursive_fib(position - 2)
