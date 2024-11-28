def second_largest_num(n):
    n.sort(reverse=True)
    if len(n) < 2:
        return "Enter at least two numbers."
    else:
        largest = n[0]
        second_largest = None
        for i in n:
            if i < largest:
                second_largest = i
                break
    return second_largest

lists = list(map(int,input("Enter numbers separated by space: ").split()))
result = second_largest_num(lists)
if result is not None:
    print(f"Second largest number: {result}")
else:
    print("Invalid input. Second largest numbers are all same.")