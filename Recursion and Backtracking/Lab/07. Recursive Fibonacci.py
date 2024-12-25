
number = int(input())

def Fibonacci(number):

    if number <= 1:
        return 1

    return Fibonacci(number - 1) + Fibonacci(number - 2)



print(Fibonacci(number))
