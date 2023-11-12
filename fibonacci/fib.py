def fib(position: int) -> int:
    fib_sequence = [0, 1]

    if position < 2:
        return fib_sequence[position]

    for i in range(2, position + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

    return fib_sequence[position]
