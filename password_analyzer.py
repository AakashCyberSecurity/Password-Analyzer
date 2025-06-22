import re
import string

common_passwords = ['123456', 'password', '12345678', 'qwerty', 'abc123']

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❗ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❗ Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❗ Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❗ Add at least one number.")

    if re.search(r"[" + re.escape(string.punctuation) + "]", password):
        score += 1
    else:
        feedback.append("❗ Add at least one special character.")

    if password.lower() in common_passwords:
        feedback.append("❗ Avoid common passwords.")

    return score, feedback

def analyze():
    password = input("🔐 Enter your password to analyze: ")
    score, feedback = check_password_strength(password)

    print("\n🔍 Password Analysis Result:")
    print("✅ Strength Score: {}/5".format(score))
    if score == 5:
        print("🎉 Strong password!")
    else:
        for msg in feedback:
            print(msg)

if __name__ == "__main__":
    analyze()
