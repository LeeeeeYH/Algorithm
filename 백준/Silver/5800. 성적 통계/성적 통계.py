input = __import__('sys').stdin.readline

K = int(input())
ls = [sorted(list(map(int, input().split()))[1:]) for _ in range(K)]

for i in range(K):
    print("Class", i+1)
    print("Max ", ls[i][-1], ", Min ", ls[i][0], ", Largest gap ", max([ls[i][j+1]-ls[i][j] for j in range(len(ls[i])-1)]), sep="")