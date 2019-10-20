from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    # Check that the input is a postive integer
    if type(n) != int:
        raise TypeError('n must be a positive int')
    if n < 1:
        raise TypeError('n must be positive init')

    #Compute the Nth term
    if n == 1:
       return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)

for n in range(1, 51):
    print(fibonacci(n))

print(fibonacci(True))
