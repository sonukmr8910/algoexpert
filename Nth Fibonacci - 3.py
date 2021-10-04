# Time: O(n)
# Space: O(n)

def fib(n, mem={1: 0, 2: 1}):
    if n in mem:
        return mem[n]
    else:
        mem[n] = fib(n-1, mem) + fib(n-2, mem)
        return mem[n]


# Test 1: Expected = 3
n = 5
print('Fibonacci of {} is {}'.format(n, fib(n)))

# Test 2: Expected = 46368
n = 25
print('Fibonacci of {} is {}'.format(n, fib(n)))
