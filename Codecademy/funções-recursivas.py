def fatorial(n: int) -> int:
    if n == 1:
        return 1
    return n * fatorial(n-1)

fat5 = fatorial(5)
print(fat5)