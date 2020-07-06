
# Recursive Solution
fibArray = [None, 1, 1]
def fib(n):
    if n < 1:
        return 0
    if n < len(fibArray):
        return fibArray[n]
    else:
        result = fib(n - 1) + fib(n - 2)
        print(fibArray, n)
        fibArray[n] = result
        return result

# "Bottom-Up" Solution
def fib_bottom_up(n):
    if n < 1:
        return None
    if n == 1 or n == 2:
        return 1

    arr = [None] * (n + 1)

    arr[1] = 1
    arr[2] = 2

    for i in range(3, n + 1):
        print(arr, i)
        arr[i] = arr[i - 1] + arr[i - 2]
        print(arr[i])

    return arr[n]


print(fib_bottom_up(100))
