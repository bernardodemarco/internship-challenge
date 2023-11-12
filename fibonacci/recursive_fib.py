def recursive_fib(position: int) -> int:
    if position == 0:
        return 0
    
    if position == 1:
        return 1
    
    return recursive_fib(position - 1) + recursive_fib(position - 2)
