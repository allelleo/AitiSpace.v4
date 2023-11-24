m, n, k = list(map(int, input().split(' ')))
coins = 0
print(m, n, k, sep='\n')

while not m < n:
    m = m - n
    coins += n // k
    m += n % k
print(coins)