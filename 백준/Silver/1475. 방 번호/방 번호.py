import sys
input = sys.stdin.readline

N = input().rstrip()
ls = [0]*9
sixnine = 0

for i in N:
    if i == '6' or i == '9':
        sixnine += 1
    else:
        ls[int(i)] += 1

sixnine = (sixnine+1) // 2
print(max(max(ls), sixnine))