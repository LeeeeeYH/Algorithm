import sys
from collections import defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
pre_dict = defaultdict(int)
pre_dict[0] = 1

adding = 0
count = 0

for i in A:
    adding += i
    count += pre_dict[adding - K]
    pre_dict[adding] += 1

print(count)