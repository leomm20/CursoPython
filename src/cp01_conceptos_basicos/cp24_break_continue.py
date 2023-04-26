# break y continue sirven para while y for

# ejemplos con while
nro = 1
while nro != 10:
    print(nro)
    if nro == 3:
        break
    nro += 1
print()

nro = 0
while nro != 5:
    nro += 1
    if nro == 3:
        continue
    print(nro)
