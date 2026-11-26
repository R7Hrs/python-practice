a = input("First value: ").lower() in ("1", "true")
b = input("Second value: ").lower() in ("1", "true")

result = (a and b) or (not a and not b)

print(int(result))