input = __import__('sys').stdin.readline

ls = [0]*47
ls[1], ls[2] = 0, 1
for i in range(3, 47):
    ls[i] = ls[i-1] + ls[i-2]
print(ls[int(input())+1])