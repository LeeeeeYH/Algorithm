input = __import__('sys').stdin.readline
summ = 0
nums = [0]*100
for _ in range(10):
    N = int(input())
    summ += N
    nums[N//10] += 1
print(summ//10)
most, res = 0, 0
for i in range(1, 100):
    if most < nums[i]:
        most = nums[i]
        res = i*10
print(res)