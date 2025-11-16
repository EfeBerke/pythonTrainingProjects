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