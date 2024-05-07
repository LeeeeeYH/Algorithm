input = __import__('sys').stdin.readline
yut = ['D','C','B','A','E']

for _ in range(3):
    print(yut[sum(map(int, input().split()))])