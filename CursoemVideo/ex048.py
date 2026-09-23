s = 0
n = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        s += c
        n += 1
print(f'A somas dos {n} números é {s}')