#Fibonacci Sequence
def fibonacci_sequence(limit):
    fib_sequence = [0, 1] 
    while fib_sequence[-1] + fib_sequence[-2] <= limit:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


fib_sequence = fibonacci_sequence(100)
print(fib_sequence)
