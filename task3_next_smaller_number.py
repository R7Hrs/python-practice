n = int(input("Enter a positive number: "))

digits = sorted(str(n))
answer = -1

x = n - 1
while x > 0:
    if sorted(str(x)) == digits:
        answer = x
        break
    x = x - 1

print(answer)