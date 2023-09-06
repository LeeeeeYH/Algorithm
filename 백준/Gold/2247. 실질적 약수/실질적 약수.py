import sys
input = sys.stdin.readline

n = int(input())
csod = 0
for i in range(2, int(n**0.5)+1):
    a = n//i
    csod += i + i*(a-i) + (i+1+a)*(a-i)//2
    # csod += i + i*(n//i-i) + max(0, (i+1+n//i)*(n//i-i)//2)   # {i+1 ~ n//i합}

print(csod % 1_000_000)