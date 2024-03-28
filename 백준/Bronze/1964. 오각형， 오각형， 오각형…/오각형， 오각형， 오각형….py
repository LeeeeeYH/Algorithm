N = int(__import__('sys').stdin.readline())
res = 1
for i in range(1, N+1):
    res += 3*i + 1
print(res%45678)