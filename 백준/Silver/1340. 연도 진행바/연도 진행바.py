import sys
input = sys.stdin.readline

mon, d, y, t = input().split()
d, y = int(d[:-1]), int(y)
h, m = map(int, t.split(':'))

all = 365*24*60

name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
dal = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if y%400==0 or (y%4==0 and y%100):
    all += 24*60
    dal[2] += 1
for i in range(2, 13):
    dal[i] += dal[i-1]
now = dal[name.index(mon)]*24*60 + (d-1)*24*60 + h*60 + m

print(now/all*100)