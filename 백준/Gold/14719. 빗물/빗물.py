import sys
input = sys.stdin.readline

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

res = 0
high = blocks[0]
water = 0
for i in range(1, W):
    if blocks[i] < high:
        water += high-blocks[i]
    else:
        res += water
        water = 0
        high = blocks[i]

high = blocks[W-1]
water = 0
for i in range(W-2, -1, -1):
    if blocks[i] < high:
        water += high-blocks[i]
    elif blocks[i] > high:
        res += water
        water = 0
        high = blocks[i]

print(res)