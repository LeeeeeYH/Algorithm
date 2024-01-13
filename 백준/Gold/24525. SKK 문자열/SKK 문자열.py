import sys
input = sys.stdin.readline

string = ' ' + input().rstrip()
leng = len(string)-1
s, k, score = [0]*(leng+1), [0]*(leng+1), [0]*(leng+1)
first = dict()

for i in range(1, leng+1):
    s[i], k[i], score[i] = s[i-1], k[i-1], score[i-1]
    if string[i] == 'S':
        s[i] += 1
        score[i] += 2
    if string[i] == 'K':
        k[i] += 1
        score[i] -= 1

res = -1
for i in range(leng+1):
    cur = score[i]
    if cur in first:
        if s[first[cur]] != s[i] and k[first[cur]] != k[i]:
            res = max(res, i - first[cur])
    else:
        first[cur] = i

print(res)