import sys
input = sys.stdin.readline

ls = [int(input()) for i in range(10)]
res = 0
for i in ls:
    if abs(100 - res) >= abs(100 - res - i):
        res += i
    else:
        break

print(res)