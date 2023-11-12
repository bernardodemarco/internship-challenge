from fibonacci.main import run_fib
from prime_numbers.main import run_primes

def run() -> None:
    while True:
        problems_options = {
            '1': run_fib,
            '2': run_primes
        }

        print('Which problem would you like to solve?')
        print('FIBONACCI     (1)')
        print('PRIME NUMBERS (2)')
        problem = input().strip()
        while not problem.isdecimal() or (problem != '1' and problem != '2'):
            problem = input('Invalid input! Enter either 1 in order to solve the FIBONACCI problem or 2 to solve the PRIME NUMBERS problem: ').strip()

        func = problems_options[problem]
        func()

        run_again = input('\nWould you like to run any problem solution again? (y/n) ').strip().lower()
        while run_again != 'y' and run_again != 'n':
            run_again = input('Invalid input! Would you like to run any problem solution again? (y/n) ').strip().lower()
        
        if run_again == 'n':
            break

if __name__ == '__main__':
    run()