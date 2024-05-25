input = __import__('sys').stdin.readline

for _ in range(int(input())):
    x, y = 0, 0
    for _ in range(int(input())):
        a, b = input().split()
        if a == 'R':
            if b == 'P':
                y += 1
            elif b == 'S':
                x += 1
        elif a == 'P':
            if b == 'R':
                x += 1
            elif b == 'S':
                y += 1
        else:
            if b == 'R':
                y += 1
            elif b == 'P':
                x += 1

    if x > y:
        print("Player 1")
    elif x < y:
        print("Player 2")
    else:
        print("TIE")