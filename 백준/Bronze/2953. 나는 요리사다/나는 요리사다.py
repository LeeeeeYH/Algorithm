input = __import__('sys').stdin.readline

resi, res = 0, 0
for i in range(5):
    summ = sum(map(int, input().split()))
    if res < summ:
        resi, res = i+1, summ
print(resi, res)