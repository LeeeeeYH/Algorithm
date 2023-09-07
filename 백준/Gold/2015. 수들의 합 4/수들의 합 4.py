N, K = map(int, input().split())
A = list(map(int, input().split()))
sum_dict = dict()
sum_num = 0
res = 0
for i in A:
    sum_num += i
    if sum_num == K: res += 1
    if sum_dict.get(sum_num - K) is not None:
        res += sum_dict.get(sum_num - K)

    if sum_dict.get(sum_num) is None:
        sum_dict[sum_num] = 1
    else:
        sum_dict[sum_num] += 1
print(res)