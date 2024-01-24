import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    ls = sorted(map(int, input().split()))
    res = 0
    for i in range(N-2):
        k = i+2
        for j in range(i+1, N-1):
            while k < N:
                left = ls[j] - ls[i]
                right = ls[k] - ls[j]
                if left > right:
                    k += 1
                elif left == right:
                    res += 1
                    break
                else:  # left < right
                    break
    print(res)