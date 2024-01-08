import sys
input = sys.stdin.readline


N = int(input())
ls = list(map(int, input().split()))
max_num = 1000004

# 에라모르게따 체
prime = [False]*2 + [True]*max_num
for i in range(2, int(max_num**0.5)+1):
    if prime[i]:
        for j in range(i+i, max_num+1, i):
            prime[j] = False

yaksus = []  # 사용된 소인수들
jisus = []  # N개의 숫자별[그 소인수의][지수들]

num = 2
while True:
    if prime[num]:  # 소수여야 소인수 후보
        if max(ls) < num:  # 다 나눠서 소인수가 더 커지면
            break  # 중단

        jisu_cnt = [0]*N  # 소인수별로 지수 세보고 있으면 추가할 임시배열
        for i in range(N):  # N개 숫자 각각
            while ls[i] % num == 0:  # num으로 나눠지네?
                jisu_cnt[i] += 1  # 추가
                ls[i] //= num  # 그 숫자는 나누기

        if max(jisu_cnt) >= 1:  # num으로 나눠지는 숫자가 존재하면
            yaksus.append(num)  # 소인수종류 추가
            jisus.append(jisu_cnt)  # 그 소인수가 몇개씩 있나

    num += 1  # 소인수 증가

res, cnt = 1, 0
for yaksu, jisu in zip(yaksus, jisus):
    summ = sum(jisu)  # 다 더해서
    all = summ // N  # 고르게 나눠가지면
    jisu.sort()  # 최소값 구하고, 계산 중 중단하기 위해 정렬
    if jisu[0] < all:  # 최소값을 올릴 수 있을 때
        for i in range(N):
            if jisu[i] < all:  # 부족한 것들은
                cnt += all - jisu[i]  # 상근이의 행동으로 받는다
            else:  # 같거나 넘어가는 순간 계산 안해도됨
                break

    res *= yaksu ** all  # 최소 값이므로 최대공약수에 더해주자

print(res, cnt)