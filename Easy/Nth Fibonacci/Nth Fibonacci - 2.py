# Time: O(2^n)
# Space: O(n)

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# Test 1: Expected = 3
n = 5
print('Fibonacci of {} is {}'.format(n, fib(n)))

# Test 2: Expected = 46368
n = 25
print('Fibonacci of {} is {}'.format(n, fib(n)))
