import sys
input = sys.stdin.readline

k = int(input())
eq = list(map(str, input().split()))
maxnum, minnum = '0'*(k+1), '9'*(k+1)

def recur(cur, num, check):
    global maxnum, minnum
    if cur == k:
        maxnum = max(maxnum, num)
        minnum = min(minnum, num)
        return

    if eq[cur] == '<':
        for i in range(int(num[-1]) + 1, 10):
            if not check & 1<<i:
                recur(cur + 1, num + str(i), check | 1<<i)
    else: # eq[cur] == '>':
        for i in range(int(num[-1])):
            if not check & 1<<i:
                recur(cur + 1, num + str(i), check | 1<<i)

for i in range(10):
    recur(0, str(i), 1<<i)

print(maxnum)
print(minnum)