import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    ls = list(map(int, input().split()))
    max_num = max(ls)
    summ = sum(ls)

    for num in range(max_num, summ+1):  # ls의 최솟값부터 전체 합까지가 후보
        minisum, cnt = 0, 0  # 계속 더해가면서 num이 되는지 확인, 합쳐야 할 횟수
        for i in ls:
            minisum += i
            if minisum < num:
                cnt += 1
            elif minisum > num:
                cnt = -1  # 불가능 표시
                break
            else:
                minisum = 0
        else:
            if minisum == 0:
                print(cnt)
                break