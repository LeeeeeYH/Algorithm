import sys
input = sys.stdin.readline
mbtis = ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP", "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]

T = int(input())
for _ in range(T):
    N = int(input())
    ls = list(map(str, input().split()))
    if N > 32:
        print(0)
    else:
        res = 99999
        # 3명 뽑는 조합
        def recur(cur, start, arr):
            if cur == 3:
                global res
                res = min(res, cal(arr))
                return

            for i in range(start, N):
                recur(cur+1, i+1, arr+[ls[i]])

        # 뽑힌 3명의 심리 거리 계산
        def cal(arr):
            ret = 0
            for i in range(4):
                if arr[0][i] != arr[1][i]:
                    ret += 1
                if arr[1][i] != arr[2][i]:
                    ret += 1
                if arr[2][i] != arr[0][i]:
                    ret += 1
            return ret

        recur(0, 0, [])
        print(res)