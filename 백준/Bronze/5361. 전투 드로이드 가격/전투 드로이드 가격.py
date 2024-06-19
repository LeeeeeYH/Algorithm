input = __import__('sys').stdin.readline
price = [350.34, 230.9, 190.55, 125.3, 180.9]

for _ in range(int(input())):
    ls = list(map(int, input().split()))
    print("$%.2f" % sum([price[i]*ls[i] for i in range(5)]))