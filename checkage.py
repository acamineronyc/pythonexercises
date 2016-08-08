age = eval(input("What is your age? "))

if (age >= 1) | (age <= 18):
    print("You are just starting life")
elif (age >= 21) | (age <= 50):
    print("You are an adult")
else:
    print("You are very old")