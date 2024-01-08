import sys
input = sys.stdin.readline

n, k = map(int, input().split())
one = n - k  # gcd > 1만족 하지 않는 개수

if one == 0:  # 1때문에 모두 만족하지 않을 순 없음
    print("Impossible")
elif one % 2 == 0:  # one만큼 두개씩 바꾸고 나머지 그대로
    for i in range(one//2):
        print(i*2+2, i*2+1, end=" ")
    for i in range(one+1, n+1):
        print(i, end=" ")
else: # 1은 그대로, 2부터 두개씩 바꾸고 나머지 그대로
    print(1, end=" ")
    for i in range(one//2):
        print(i*2+3, i*2+2, end=" ")
    for i in range(one+1, n+1):
        print(i, end=" ")
