# 소수의 자격
A, B, D = map(int, input().split())
D = str(D)
is_prime = [0] + [0] + [1]*(B-1)

# 에라모르게따
for i in range(2, int(B**0.5)+1):
    if is_prime[i]:
        for j in range(i+i, B+1, i):
            is_prime[j] = 0

cnt = 0
for i in range(A, B+1):
    if is_prime[i] and D in str(i):
       cnt += 1
print(cnt)