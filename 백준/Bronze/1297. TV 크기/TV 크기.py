input = __import__('sys').stdin.readline

D, H, W = map(int, input().split())
r = D/(H*H+W*W)**0.5
print(int(H*r), int(W*r))