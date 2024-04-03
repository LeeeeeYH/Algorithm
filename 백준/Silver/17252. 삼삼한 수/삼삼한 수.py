input = __import__('sys').stdin.readline

N = int(input())
if N == 0:
    print('NO')
    exit(0)
def three(num):
    ret = ''
    while num:
        num, mod = divmod(num, 3)
        ret += str(mod)
    return ret[::-1]
print('NO' if '2' in three(N) else 'YES')