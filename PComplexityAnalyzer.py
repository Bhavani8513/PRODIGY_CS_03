import re

def password_complexity_checker(password):

    feedback = []
    strength = "weak"

    # Check length
    if len(password) < 12:
        feedback.append("Password is too short. It should be at least 12 characters.")
    else:
        strength = "medium"

    # Check uppercase letters
    if not re.search(r"[A-Z]", password):
        feedback.append("Password should contain at least one uppercase letter.")
    else:
        strength = "strong" if strength == "medium" else strength

    # Check lowercase letters
    if not re.search(r"[a-z]", password):
        feedback.append("Password should contain at least one lowercase letter.")
    else:
        strength = "strong" if strength == "medium" else strength

    # Check numbers
    if not re.search(r"\d", password):
        feedback.append("Password should contain at least one number.")
    else:
        strength = "strong" if strength == "medium" else strength

    # Check special characters
    if not re.search(r"[!@#$%^&*()+=-{};:'<>,./?]", password):
        feedback.append("Password should contain at least one special character.")
    else:
        strength = "strong" if strength == "medium" else strength

    return {"strength": strength, "feedback": feedback}

def main():
    password = input("Enter a password: ")
    result = password_complexity_checker(password)
    print(f"Password strength: {result['strength']}")
    if result['feedback']:
        print("Feedback:")
        for item in result['feedback']:
            print(f"- {item}")

if __name__ == "__main__":
    main()