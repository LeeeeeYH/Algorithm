input = __import__('sys').stdin.readline

N = int(input())
ls = [0] + list(map(int, input().split()))
cycle = [0]*(N+1)
for i in range(1, N+1):
    cnt = 1
    num = ls[i]
    while num != i:
        num = ls[num]
        cnt += 1
    cycle[i] = cnt

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
def lcm(a, b):
    return a*b//gcd(a,b)

res = cycle[1]
for i in range(2, N+1):
    res = lcm(res, cycle[i])
print(res)