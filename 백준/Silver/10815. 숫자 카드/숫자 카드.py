import sys
input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
nums = list(map(int, input().split()))

for num in nums:
    i, j = 0, N-1
    while i <= j:
        mid = (i+j)//2
        if cards[mid] < num:
            i = mid + 1
        elif cards[mid] > num:
            j = mid - 1
        else: # cards[mid] == num:
            print(1, end=' ')
            break
    else:
        print(0, end=' ')