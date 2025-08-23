# age = int(input("Enter your age: "))

# if age >= 100:
#     print("You are too old to vote.")
# elif age >= 18:
#     print("You are eligible to vote.")
# elif age < 0:
#     print("Invalid age.")
# # elif age >= 100:
#     # print("You are too old to vote.")
# else:
#     print("Your are not eligible to vote.")


response = input("Do you want a food? (Y/N): ")

if response == "Y":
    print("Here is your food,")
elif response == "N":
    print("Okay, no food for you.")
else:
    print("Invalid iinput. Please enter Y or N.")