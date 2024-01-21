import sys
input = sys.stdin.readline

N = int(input())
s = input().rstrip()
alpha = [0]*26
used = 0  # 사용하는 알파벳 종류 개수
i, res = 0, 0

for j in range(len(s)):
    cur = ord(s[j])-97
    if not alpha[cur]: # 처음 나오는 알파벳
        used += 1
    alpha[cur] += 1

    if used <= N:
        res = max(res, j-i+1)
    while used > N:
        bf = ord(s[i])-97
        alpha[bf] -= 1
        if alpha[bf] == 0:
            used -= 1
        i += 1

print(res)