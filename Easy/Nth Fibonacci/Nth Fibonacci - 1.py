# Time: O(n)
# Space: O(1)

def fib(n):
    last_two_fibs = [0, 1]
    counter = 3
    while counter <= n:
        next_fib = last_two_fibs[0] + last_two_fibs[1]
        last_two_fibs[0] = last_two_fibs[1]
        last_two_fibs[1] = next_fib
        counter += 1
    return last_two_fibs[1] if n > 1 else last_two_fibs[0]


# Test 1: Expected = 3
n = 5
print('Fibonacci of {} is {}'.format(n, fib(n)))

# Test 2: Expected = 46368
n = 25
print('Fibonacci of {} is {}'.format(n, fib(n)))
