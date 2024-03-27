import sys
sys.setrecursionlimit(10_000_000)
input = sys.stdin.readline

N = int(input())
graph = dict()
for _ in range(N):
    cur, l, r = input().split()
    graph[cur] = [l, r]

def pre_order(cur):
    if cur == '.':
        return

    print(cur, end='')
    pre_order(graph[cur][0])
    pre_order(graph[cur][1])

def in_order(cur):
    if cur == '.':
        return

    in_order(graph[cur][0])
    print(cur, end='')
    in_order(graph[cur][1])

def post_order(cur):
    if cur == '.':
        return

    post_order(graph[cur][0])
    post_order(graph[cur][1])
    print(cur, end='')

pre_order('A')
print()
in_order('A')
print()
post_order('A')