

liczby = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
liczby2 = []
liczby3 = []
print (liczby)


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


for x in liczby:
    for y in liczby:
        for z in liczby:
            for w in liczby:
                if x **3 + y ** 3+ z ** 3 + w ** 3 == 100:
                    liczby2.append(x)
                    liczby2.append(y)
                    liczby2.append(z)
                    liczby2.append(w)

liczby2 = [1, 1, 0, 2]
print (liczby2)
for a in list(set(liczby2)):
    for b in list(set(liczby2)):
        if (not b == a) or (a == 1 and b == 1):
            for c in list(set(liczby2)):
                if (not (c == a or c == b)) or (c == 1 and (a == 1 or b == 1)):
                    for d in list(set(liczby2)):
                        if (not (d == a or d == b or d == a)) or (d == 1 and (a == 1 or b == 1 or c == 1)):
                            liczby3.append(a * 1000 + b * 100 + c * 10 + d)

print (liczby3)

liczby2 = []
for x in liczby:
    for y in liczby:
        for z in liczby:
            for w in liczby:
                for p in liczby3:
                    if x ** 3 + y ** 3 + z ** 3 + w ** 3 == p:
                        liczby2.append(x)
                        liczby2.append(y)
                        liczby2.append(z)
                        liczby2.append(w)
print (liczby2)
