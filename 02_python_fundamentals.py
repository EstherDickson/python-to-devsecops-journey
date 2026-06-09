# INPUT + CONDITIONALS
## PROJECT 1 GREETING SYSTEM

name = input("Enter your name: ")
print(f'Hello, {name}')

## PROJECT 2 AGE CHECKER
age = int(input("Enter your age: "))
print(age)
if age >= 18:
    print("Adult")
else:
    print("Minor")

## PROJECT 3 LAPTOP CHECKER
has_laptop = input("Do you have a laptop (yes/no): ")
if has_laptop.lower() == "yes":
    print("Ready for coding")
else:
    print("Need a laptop")

## PROJECT 4 MINI CHALLENGE
name = input("Enter your name: ")
age = int(input("Enter your age: "))
career_choice = input("Do you want to be a DevSecOps Engineer?: ")
if career_choice.lower() == "yes" and age >= 18:
    print(f"Welcome {name}, congratulations to you, you are old enough to be a DevSecOps Engineer")
else:
    print(f"Sorry {name}, keep learning and growing.")