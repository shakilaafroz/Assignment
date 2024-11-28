string = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0

for i in string:
    if i in vowels:
        count += 1
print(f"Number of vowels: {count}")