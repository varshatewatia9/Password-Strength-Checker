print("=== Password Strength Checker v1.21111 ===")

password = input("Enter your password: ")
common_passwords = ["password", "123456", "qwerty", "abc123", "letmein", "monkey", "welcome", "111111", "baseball", "iloveyou"]

score = 0

if len(password) >= 8:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

special = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

if any(char in special for char in password):
    score += 1
print("="*20)
print(f"Password Score: {score}/5")
print("="*20)
percentage = (score / 5) * 100
print(f"Password Strength Percentage: {percentage:.0f}%")

print("\nSuggestions to improve your password:")
if len(password) < 8:
    print("- Use at least 8 characters.")
if not any(char.isupper() for char in password):
    print("- Include at least one uppercase letter.")
if not any(char.islower() for char in password):
    print("- Include at least one lowercase letter.")
if not any(char.isdigit() for char in password):
    print("- Include at least one digit.")
if not any(char in special for char in password):
    print("- Include at least one special character.")

print()
if password.lower() in common_passwords:
    print("Warning: Your password is a commonly used password. Consider changing it to something more unique.")

if score == 5:
    print("Very Strong Password 💪")

elif score >= 3:
    print("Strong Password 👍")
elif score == 2:
    print("Medium Password 👌")
else:
    print("Weak password ❌")

print("\nCyberSecurity tip ")
if score ==5 :
    print("Great ! Never reuse the same password again ")
elif score >=3:
    print("Consider using a password manager for stronger unique password")
else:
    print("Weak passwords are vulnerable to brute-force attacks")

print("\nThank you for using the Password Strength Checker!")
print("\nMade by Varsha Tewatia")