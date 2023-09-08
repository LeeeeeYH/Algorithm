import sys
input = sys.stdin.readline

T = int(input())
n = int(input())
A = [0] + list(map(int, input().split()))
m = int(input())
B = [0] + list(map(int, input().split()))
# 입력 끝

# A 누적합
sumA = [0] * (n + 1)
for i in range(1, n+1):
    sumA[i] = A[i] + sumA[i - 1]
dictA = dict() # 누적합의 dict

# 값들 dict에 저장
for i in range(n):
    for j in range(i+1, n+1):
        tmp_sub = sumA[j] - sumA[i]
        if dictA.get(tmp_sub) is None:
            dictA[tmp_sub] = 1
        else:
            dictA[tmp_sub] += 1
            
# B 누적합
sumB = [0] * (m + 1)
for i in range(1, m+1):
    sumB[i] = B[i] + sumB[i - 1]

res = 0
for i in range(m):
    for j in range(i+1, m+1):
        tmp_sub = sumB[j] - sumB[i] # B의 특정 부 배열에 대해서
        if dictA.get(T - tmp_sub) is not None: # A의 부배열 + B의 부배열 = T인 것이 dict에 저장되어 있었다면
            res += dictA[T - tmp_sub] # 그만큼 더해줌

print(res)