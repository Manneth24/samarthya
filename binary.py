def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def find_primes(limit):
    primes = []
    for i in range(2, limit+1):
        if is_prime(i):
            primes.append(i)
    return primes

limit = int(input("Enter the limit: "))
print("The prime numbers up to", limit, "are:")
print(find_primes(limit))