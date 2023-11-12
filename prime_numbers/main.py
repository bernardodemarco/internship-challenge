from typing import List, Callable

from is_prime import is_prime
from recursive_is_prime import recursive_is_prime


def get_prime_numbers_up_to_target(target: int, func: Callable[[int], bool]) -> List[int]:
    prime_numbers = []
    current_num = 0
    while current_num <= target:
        if func(current_num):
            prime_numbers.append(current_num)
        
        current_num += 1

    return prime_numbers

def run() -> None:
    algorithms_options = {
        '1': is_prime,
        '2': recursive_is_prime
    }

    while True:
        number = input('Enter an integer number greater than 1: ').strip()
        while not number.isdecimal() or int(number) <= 1:
            number = input('Invalid input! Enter an integer number greater than 1: ').strip()
        number = int(number)
        
        print('Which algorithm would you like to test?')
        print('LINEAR ALGORITHM    (1)')
        print('RECURSIVE ALGORITHM (2)')
        algorithm = input().strip()
        while not algorithm.isdecimal() or (algorithm != '1' and algorithm != '2'):
            algorithm = input('Invalid input! Enter either 1 in order to run the LINEAR ALGORITHM or 2 to run the RECURSIVE ALGORITHM: ').strip()
        
        func = algorithms_options[algorithm]
        prime_numbers = get_prime_numbers_up_to_target(number, func)
        print(f'\np({number}) = {prime_numbers}\n')

        run_again = input('Would you like to run the algorithm again? (y/n) ').strip().lower()
        while run_again != 'y' and run_again != 'n':
            run_again = input('Invalid input! Would you like to run the algorithm again? (y/n) ').strip().lower()
        
        if run_again == 'n':
            break


if __name__ == '__main__':
    run()