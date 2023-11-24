magic = []
n = int(input())
if n == 0:
    print(0)
    exit()
if n > 9 * 3:
    raise ValueError

pairs = []

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i + j + k == n:
                if not [i, j, k] in pairs:
                    pairs.append([i, j, k])
print(len(pairs))
