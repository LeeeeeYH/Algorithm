import sys
input = sys.stdin.readline

colors = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
print((colors.index(input().rstrip())*10 + colors.index(input().rstrip())) * 10**colors.index(input().rstrip()))