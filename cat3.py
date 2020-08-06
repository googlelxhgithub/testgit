
n = int(input())
c = 0

for i in range(n+1):
    if str(i).count("3") != 0 or i % 3 == 0:
        continue
    else:
        c += 1

print(c)