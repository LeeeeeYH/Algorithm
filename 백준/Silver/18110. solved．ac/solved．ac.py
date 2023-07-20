import sys
input = sys.stdin.readline

def round(num):
    return int(num+0.5)

n = int(input())
cut = int(round(n*0.15))
ls = sorted([int(input()) for _ in range(n)])
if cut >= 1:
    ls = ls[cut:-cut]
print(0 if len(ls) == 0 else round(sum(ls)/len(ls)))