print("=== Password Strength Checker v1.1 ===")

password = input("Enter your password: ")

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

if score == 5:
    print("Very Strong Password 💪")

elif score >= 3:
    print("Strong Password 👍")
elif score == 2:
    print("Medium Password 👌")
else:
    print("Weak password ❌")
print("\nMade by Varsha Tewatia")