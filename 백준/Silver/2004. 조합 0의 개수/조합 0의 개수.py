import sys
input = sys.stdin.readline

n, m = map(int, input().split())

twos, fives = 0, 0
two, five = 2, 5
while two <= n:
    twos += n//two - (n-m)//two - m//two
    two *= 2

while five <= n:
    fives += n//five - (n-m)//five - m//five
    five *= 5

print(min(twos, fives))