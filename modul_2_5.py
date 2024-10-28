numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes_ = []
not_primes = []
primes = [i for i in range(len(numbers) + 1)]
primes[1] = 0
i = 2
while i <= len(numbers):
    if primes[i] != 0:
        j = i + i
        while j <= len(numbers):
            primes[j] = 0
            j = j + i
    i += 1
primes_ = [i for i in primes if i != 0]
print('Primes:', primes_)
not_primes = [i for i in numbers if i not in primes_ and i != 1]
print('Not_primes:', not_primes)