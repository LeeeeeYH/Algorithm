# 최대 GCD
def GCD(a, b): # a >= b 보장
    while a % b:
        a, b = b, a % b
    return b

T = int(input())
for _ in range(T):
    nums = sorted(list(map(int, input().split())))
    leng = len(nums)
    max_GCD = 0
    for i in range(leng-1):
        for j in range(i+1, leng):
            max_GCD = max(max_GCD, GCD(nums[j], nums[i]))
    print(max_GCD)