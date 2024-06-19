#Write a python program that generates the first n numbers in the Fibonacci sequence.
def generate_fibo(n):
    sequence=[0,1]
    for i in range (2,n):
        next_num=sequence[-2]+sequence[-1]
        sequence.append(next_num)
    return sequence
n=int(input("Enter the number of Fibonacci numbers to generate: "))
print(f"Fibonacci Series of {n} numbers")
print(generate_fibo(n))