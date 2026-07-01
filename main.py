import random 
import hashlib
import requests
import os 
import getpass

def check_password_breach(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()

    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    url = "https://api.pwnedpasswords.com/range/" + prefix

    response = requests.get(url)

    if response.status_code != 200:
        print("Could not connect to breach database.")
        return

    hashes = response.text.splitlines()

    for line in hashes:
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            print("\n⚠ WARNING!")
            print(f"This password has appeared in {count} data breaches.")
            print("Please choose a different and more unique password.")
            return

    print("\n✅ Good news!")
    print("This password was NOT found in the breach database.")

print("=== Password Strength Checker v1.21111 ===")

name = input("Enter your name: ").lower()
email = input("Enter your email: ").lower()
password = getpass.getpass("Enter your password: ")

password_hash = hashlib.sha256(password.encode()).hexdigest()

history_file = "password_history.txt"

if os.path.exists(history_file):
    with open(history_file, "r") as file:
        previous_passwords = file.read().splitlines()

    if password_hash in previous_passwords:
        print("\n⚠ Warning: You have already used this password before.")
        print("Reusing passwords is not recommended.")

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

check_password_breach(password)

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
if name in password.lower() :
    print("Warning: Your password contains your name. Consider changing it to something more unique.")
if email in password.lower() :
    print("Warning: Your password contains your email. Consider changing it to something more unique.")

if score == 5:
    strength = "Very Strong Password "
elif score == 4:
    strength = "Strong Password "
elif score >= 2:
    strength = "Medium Password "
else:
    strength = "Weak password "
print(strength)

print("\nCyberSecurity tip ")
if score ==5 :
    print("Great ! Never reuse the same password again ")
elif score >=3:
    print("Consider using a password manager for stronger unique password")
else:
    print("Weak passwords are vulnerable to brute-force attacks")

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"  
symbols = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
all_charachters = letters+numbers+symbols
generated_password = "" 
for _ in range(12):
    generated_password += random.choice(all_charachters)
print("\nGenerated Password:" , generated_password)

save = input("Do you want to save the password report to a file? (yes/no): ")
if save.lower()=="yes":
    file=open("password_report.txt","a")
    file.write("\n=========Password Report=========\n")
    file.write(f"Password : {password}\n")
    file.write(f"Password Score: {score}/5\n")
    file.write(f"Strength : {strength}\n")
    file.write("=================================\n")
    file.close()
    with open(history_file, "a") as file:
        file.write(password_hash + "\n")
    print("\nPassword report saved to password_report.txt")

print("\nThank you for using the Password Strength Checker!")
print("Made by Varsha Tewatia")
