
for i in range(100):
    password = input("Enter password (or 'stop' to exit): ")

    if password == "stop":
        print("Program stopped.")
        break

    upper = 0
    lower = 0
    digit = 0

    for ch in password:
        if ch.isupper():
            upper = 1
        if ch.islower():
            lower = 1
        if ch.isdigit():
            digit = 1

    if len(password) >= 8 and upper and lower and digit:
        print("Strong password")
    else:
        print("Weak password")