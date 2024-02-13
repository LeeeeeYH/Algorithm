import sys
input = sys.stdin.readline

corrects = list(map(int, input().split()))
res = 0

def recur(cur, correct, bf_ans, con_ans): # cur, 맞은개수, 이전 답, 연속답 개수
    if cur - correct > 5: # 10 - cur < 5 - correct: 남은 문제보다 맞출 문제가 더 많으면
        return
    if cur == 10:
        global res
        res += 1
        return

    for i in range(1, 6):
        if i == bf_ans: # 이전꺼랑 같고
            if con_ans <= 1: # 그걸 0번, 1번 사용했으면 일단 가능
                if corrects[cur] == i: # 답이면
                    recur(cur+1, correct+1, bf_ans, con_ans+1)
                else: # 답이 아니면
                    recur(cur+1, correct, bf_ans, con_ans+1)
        else:
            if corrects[cur] == i: # 답이면
                recur(cur+1, correct+1, i, 1)
            else: # 답이 아니면
                recur(cur+1, correct, i, 1)

recur(0, 0, -1, 0)
print(res)