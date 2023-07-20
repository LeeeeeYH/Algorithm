# 뒤집어진 소수
def check_prime(num):
    if num == 1: return False
    if num == 2: return True
    if num % 2 == 0: return False

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

turned = ['0', '1', '2', '-1', '-1', '5', '9', '-1', '8', '6']

N = input()
# 소수가 아니거나 뒤집었을때 숫자가 안되면
if not check_prime(int(N)) or '-1' in [turned[int(i)] for i in list(N)]:
    print('no')
else: # 소수고 뒤집었을때 숫자가 되면
    # 뒤집은 수도 소수면
    if check_prime(int(''.join(turned[int(i)] for i in (N[::-1])))):
        print('yes')
    else:
        print('no')