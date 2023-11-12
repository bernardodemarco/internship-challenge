'''
1 - Fibonnaci
    -- Criar uma função em sua linguagem preferida. A função deve receber um numero N >= 0 (deve validar o input para a função), e retornar o valor correspondente desse número na sequencia fibonnaci. EX. fib(0) =0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.
    --- Criar uma função recursiva que resolva fibonacci
    --- Criar uma função linear que resolva fibonnaci
'''

def recursive_fib(position: int) -> int:
    if position == 0:
        return 0
    
    if position == 1:
        return 1
    
    return recursive_fib(position - 1) + recursive_fib(position - 2)

def fib(position: int) -> int:
    fib_sequence = [0, 1]

    if position < 2:
        return fib_sequence[position]

    for i in range(2, position + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

    return fib_sequence[position]

position = int(input())
print('RECURSIVE IMPLEMENTATION =', recursive_fib(position))
print('LINEAR IMPLEMENTATION =', fib(position))