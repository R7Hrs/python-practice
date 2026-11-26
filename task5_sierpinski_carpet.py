n = int(input("Depth n: "))

for row in range(3 ** n):
    for col in range(3 ** n):
        ch = "#"
        for i in range(n):
            if row // 3 ** i % 3 == 1 and col // 3 ** i % 3 == 1:
                ch = " "
        print(ch, end="")
    print()