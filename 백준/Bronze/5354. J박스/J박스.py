input = __import__('sys').stdin.readline

for _ in range(int(input())):
    N = int(input())
    if N == 1:
        print('#')
    else:
        print('#'*N)
        for _ in range(N-2):
            print('#'+'J'*(N-2)+'#')
        print('#'*N)
    print()