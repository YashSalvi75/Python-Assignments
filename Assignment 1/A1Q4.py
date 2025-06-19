def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def primes_in_range(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end+1):
        if is_prime(num):
            print(num, end=' ')
    print()

 
primes_in_range(10, 30)
