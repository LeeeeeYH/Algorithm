input = __import__('sys').stdin.readline

w = [4, 2, 3, 3, 3, 3, 3, 3, 3, 3]
while True:
    N = input().rstrip()
    if N == '0': break
    print(len(N)+1 + sum([w[int(i)] for i in N]))