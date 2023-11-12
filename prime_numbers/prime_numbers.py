'''
2 - Números primos
    -- A função deve receber um numero N > 1 (validar o input), e retornar todos os números primos até o numero N. EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];
    --- Criar uma função recursiva que resolva p
    --- Criar uma função linear que resolva p

    --- REVISAR CODIGO
    - VER PONTOS DE MELHORA
    - ADICIONAR MENU
    - PASSAR FUNC GENERICA COMO PARAMETRO PARA get_prime_numbers_up_to_target
'''
import math
from typing import List


def is_prime(num: int) -> bool:
    if num < 2 or (num > 2 and num % 2 == 0):
        return False
    
    if num == 2:
        return True
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
        
    return True

def recursive_is_prime(num: int, divisor: int = 2) -> bool:
    if num < 2 or (num > 2 and num % 2 == 0):
        return False
    
    if num == 2 or divisor > math.sqrt(num):
        return True
    
    is_not_divisible = num % divisor != 0
    return is_not_divisible and recursive_is_prime(num, divisor + 1)

def get_prime_numbers_up_to_target(target: int) -> List[int]:
    prime_numbers = []
    current_num = 0
    while current_num <= target:
        if recursive_is_prime(current_num):
            prime_numbers.append(current_num)
        
        current_num += 1

    return prime_numbers

number = int(input())
print(get_prime_numbers_up_to_target(number))