input = __import__('sys').stdin.readline

A, B, C, D = map(int, input().split())
ls = list(map(int, input().split()))

for i in ls:
    dog = 0
    if 0 < i % (A+B) <= A:
        dog += 1
    if 0 < i % (C+D) <= C:
        dog += 1

    print(dog)