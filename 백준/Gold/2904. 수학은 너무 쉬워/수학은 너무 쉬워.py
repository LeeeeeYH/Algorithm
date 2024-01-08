import sys
input = sys.stdin.readline


N = int(input())
ls = list(map(int, input().split()))
max_num = 1000004

prime = [False]*2 + [True]*max_num
for i in range(2, int(max_num**0.5)+1):
    if prime[i]:
        for j in range(i+i, max_num+1, i):
            prime[j] = False

yaksus = []
jisus = []

num = 2
while True:
    if prime[num]:
        if max(ls) < num:
            break

        jisu_cnt = [0]*N
        for i in range(N):
            while ls[i] % num == 0:
                jisu_cnt[i] += 1
                ls[i] //= num

        if max(jisu_cnt) >= 1:
            yaksus.append(num)
            jisus.append(jisu_cnt)

    num += 1

res, cnt = 1, 0
for yaksu, jisu in zip(yaksus, jisus):
    summ = sum(jisu)
    all = summ // N  # 고르게 나눠가지면
    jisu.sort()
    if jisu[0] < all:  # 최소값을 올릴 수 있을 때
        for i in range(N):
            if jisu[i] < all:  # 부족한 것들은
                cnt += all - jisu[i]  # 받는다

    res *= yaksu ** all

print(res, cnt)
