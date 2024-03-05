input = __import__('sys').stdin.readline

scenario = 1
while True:
    die = False
    o, w = map(int, input().split())
    if o == 0 and w == 0:
        break

    while True:
        do, n = input().split()
        n = int(n)
        if do == 'E':
            w -= n
            if w <= 0:
                die = True
        elif do == 'F':
            w += n
        else:
            break

    if die:
        print(scenario, "RIP")
    else:
        if o/2 < w < o*2:
            print(scenario, ":-)")
        else:
            print(scenario, ":-(")
    scenario += 1