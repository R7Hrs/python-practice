r = [[]]
for x in eval(input("Set: ")):
    if [x] not in r:
        r += [t + [x] for t in r]

print(sorted(r, key=len))