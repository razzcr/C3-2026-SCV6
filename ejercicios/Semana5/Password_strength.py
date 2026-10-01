#Password classification


password_length = int(input("Password length: "))
passowrd_has_number = input("Contains at least one number? (yes/no): ") == "yes"
passowrd_has_uppercase = input("Contains at least one uppercase letter? (yes/no): ") == "yes"
passowrd_has_special_char = input("Contains at least one special character? (yes/no): ") == "yes"

if password_length < 8:
    classification = "Insufficient"
elif passowrd_has_number and passowrd_has_uppercase and passowrd_has_special_char:
    classification = "Secure"
else:
    classification = "Moderate"

print(f"Password classification: {classification}")


