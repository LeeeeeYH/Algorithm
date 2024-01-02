import sys
import math
input = sys.stdin.readline

xy = list(map(int, input().split()))
ls = [list(map(int, input().split())) for _ in range(3)]

def dis(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

print(int(min(dis(xy, ls[0])+dis(ls[0], ls[1])+dis(ls[1], ls[2]),
              dis(xy, ls[0])+dis(ls[0], ls[2])+dis(ls[2], ls[1]),
              dis(xy, ls[1])+dis(ls[1], ls[0])+dis(ls[0], ls[2]),
              dis(xy, ls[1])+dis(ls[1], ls[2])+dis(ls[2], ls[0]),
              dis(xy, ls[2])+dis(ls[2], ls[0])+dis(ls[0], ls[1]),
              dis(xy, ls[2])+dis(ls[2], ls[1])+dis(ls[1], ls[0]))))
