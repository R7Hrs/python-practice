expr = input("Enter expression: ")

variables = sorted(set(c for c in expr if c.isalpha()))
python_expr = expr.replace("!", " not ").replace("+", " or ").replace("*", " and ")

print(*variables, "result")

for i in range(2 ** len(variables)):
    bits = bin(i)[2:].zfill(len(variables))
    values = {}
    for v, b in zip(variables, bits):
        values[v] = (b == "1")
    print(*bits, int(eval(python_expr, values)))