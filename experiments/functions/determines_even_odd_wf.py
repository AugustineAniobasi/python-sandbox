# A program that determines if a number is even or odd using functions
numbers = [22, 45, 47, 49, 54] 

# function definition
def check_even_odd(number):
    if number % 2 == 0: 
        print(f"The number {number} is even")
    else:
        print(f"The number {number} is odd")

# calling the function multiple times to check if different numbers are odd or even
check_even_odd(numbers[0])  
check_even_odd(numbers[1])
check_even_odd(numbers[2])
check_even_odd(numbers[3])
check_even_odd(numbers[4])

