age = int(input("Enter your age: "))

if age < 5:
    print("You are a kid")
elif age < 18:
    print("You are in school")
    print("You are not allowed to vote")
else:
    print("You are an adult")
    print("You are allowed to vote")
