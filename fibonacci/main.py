from fibonacci.fib import fib
from fibonacci.recursive_fib import recursive_fib


def run_fib() -> None:
    algorithms_options = {
        '1': fib,
        '2': recursive_fib
    }

    while True:
        print('\nWhich FIBONACCI algorithm would you like to test?')
        print('LINEAR ALGORITHM    (1)')
        print('RECURSIVE ALGORITHM (2)')
        algorithm = input().strip()
        while not algorithm.isdecimal() or (algorithm != '1' and algorithm != '2'):
            algorithm = input('Invalid input! Enter either 1 in order to run the LINEAR ALGORITHM or 2 to run the RECURSIVE ALGORITHM: ').strip()
        
        position = input('\nEnter an integer number greater than or equal to 0: ').strip()
        while not position.isdecimal() or int(position) < 0:
            position = input('Invalid input! Enter an integer number greater than or equal to 0: ').strip()
        position = int(position)

        func = algorithms_options[algorithm]
        fibonacci_sequence = func(position)
        print(f'\nfib({position}) = {fibonacci_sequence}\n')

        run_again = input('\nWould you like to run the FIBONACCI solution again? (y/n) ').strip().lower()
        while run_again != 'y' and run_again != 'n':
            run_again = input('Invalid input! Would you like to run the FIBONACCI solution again? (y/n) ').strip().lower()
        
        if run_again == 'n':
            break
