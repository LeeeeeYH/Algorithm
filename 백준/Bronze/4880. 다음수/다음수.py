input = __import__('sys').stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a==0 and b==0 and c==0:
        break

    if b+b == a+c:
        print("AP", b-a+c)
    else:
        print("GP", b//a*c)