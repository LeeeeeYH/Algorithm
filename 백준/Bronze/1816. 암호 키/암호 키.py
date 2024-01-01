import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    num = int(input())
    if num % 2 == 0:
        print("NO")
        continue

    for i in range(3, 1000001, 2):
        if num % i == 0:
            print("NO")
            break
    else:
        print("YES")