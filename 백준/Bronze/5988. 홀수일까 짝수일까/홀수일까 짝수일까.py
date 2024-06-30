input = __import__('sys').stdin.readline
even = ['0', '2', '4', '6', '8']
for _ in range(int(input())):
    K = input().rstrip()
    if K[-1] in even:
        print("even")
    else:
        print("odd")