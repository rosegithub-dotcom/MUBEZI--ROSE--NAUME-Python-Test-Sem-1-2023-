#finding average of two numbers
def average_of_two_numbers(x,y):
    return(x+y)/2


first_number=6
second_number=4

number1 = int(input("Enter first_number:"))
number2 = int(input("enter second_ number:"))
number3 = int(input("enter third_number:"))
if number1<number2 and number1<number3:
    print(f"{number1} is less than {number2} and {number3}")
elif number2<number1 and number2<number3:
        print(f"{number2} is less than {number1} and {number3}")
else:
    print(f"{number3} is less than {number1} and {number2}")




