numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for x in numbers:
    for k in range(2, x // 2 + 1):
        if x % k == 0:
            not_primes.append(x)
            break
    else:
        primes.append(x)
print('Primes:', primes)
print('Not Primes:', not_primes)