s = input("Enter a string: ")

count = 0
for i in s:
    if i.isdigit():
        count += 1
print(f"Total digits are: {count}")
