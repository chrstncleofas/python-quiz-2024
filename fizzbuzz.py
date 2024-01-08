# 1. Iterate an integer from 1 to n,
# and 2. print "Fizz" if the number is divisible by 3,
# 3. "Buzz" if the number is divisible by 5,
# and 4. "FizzBuzz" if the number is divisible by both 3 and 5.
# 5. Otherwise, print the number.

def fizzbuzz(n: int) -> None:

    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(15)
