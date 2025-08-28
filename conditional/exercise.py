# Simple calculator program
# operator = input("Enter operator: (+,-,*,/): ")
# num1 = float(input("Enter first number:"))
# num2 = float(input("Enter second number:"))

# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#     if num2 != 0:
#         result = num1 / num2
#         print(result, 3)
#     else:
#         print("Errot, cannot divide by zero.")
# else:
#     print("Invalid operator.")


# Python weight converter

# weight = float(input("Enter your weight: "))
# unit = input("(K)g or (L)bs: ")

# if unit == "K":
#     weight = weight * 2.205
#     unit = "Lbs"
#     print(f"You are {round(weight, 3)} {unit}.")
# elif unit == "L":
#     weight = weight / 2.205
#     unit = "Kg"
#     print(f"You are {round(weight, 3)} {unit}.")
# else:
#     print("Invalid unit.")

# Python temperature converter

unit = input("Convert from (C)elsius or (F)ahrenheit: ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((temp * 9/5) + 32)
    unit = "F"
    print(f"The temperature is {round(temp, 3)} {unit}.")
elif unit == "F":
    temp = round((temp - 32) * 5/9)
    unit = "C"
    print(f"The temperature is {round(temp, 3)} {unit}.")
else:
    print("Invalid unit.")


