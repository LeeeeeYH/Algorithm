import sys
input = sys.stdin.readline

s = input().rstrip()
num = [0]*2
num[int(s[0])] = 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        num[int(s[i+1])] += 1
print(min(num))