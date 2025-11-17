def mypow(x, n):
    if n > 0:
        return x * mypow(x, n-1)
    elif n < 0:
        return 1/x * mypow(x, n+1)
    elif n == 0:
        return 1
    

def isPowerOfThree(n):
    if n <= 0:
        return False  
    elif 1 == n:
        return True
    elif abs(n) < 1:
        return False
    else:
        return isPowerOfThree(n / 3)

print(isPowerOfThree(-1))
print(mypow(2, 5))


def fastpow(x, n):
    # base case
    if n == 0:
        return 1

    # negative power
    if n < 0:
        return 1 / fastpow(x, -n)

    # even power
    if n % 2 == 0:
        half = fastpow(x, n // 2)
        return half * half

    # odd power
    else:
        return x * fastpow(x, n-1)


print(fastpow(2, -3))
print(fastpow(5, 0))
print(fastpow(2, 10))
