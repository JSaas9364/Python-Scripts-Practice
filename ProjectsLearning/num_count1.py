'''
def test_slicing(s, group_size):
    print(f"\nOriginal: {s}")
    print(f"Group size: {group_size}\n")

    for i in range(0, len(s), group_size):
        print(f"i = {i}")

    grouped = [s[i:i+group_size] for i in range(0, len(s), group_size)]

    for idx, chunk in enumerate(grouped):
        print(f"Group {idx + 1}: '{chunk}'")

    print("\nFinal:", grouped)

s = input("Enter a string: ").strip()[::-1]
group_size = int(input("Enter group size: ").strip())

test_slicing(s, group_size)

'''

x = input("string: ")[::-1]  # Reverse first
size = int(input("size: "))  # Convert to integer

formatted = ','.join(x[i:i+size] for i in range(0, len(x), size))[::-1]  # Group & reverse back

print(formatted)

