input = __import__('sys').stdin.readline

alpha = ['F','D','C','B','A']
detail = ['-','0','+']
s = input().rstrip()
print(f"{alpha.index(s[0]) + detail.index(s[1])*0.3-0.3:.1f}" if s!='F' else 0.0)