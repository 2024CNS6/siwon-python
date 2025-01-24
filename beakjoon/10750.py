import sys
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
l = []
b_len = len(b)

for char in a:
    l.append(char)
    if len(l) >= b_len and ''.join(l[-b_len:]) == b:
        del l[-b_len:]

result = ''.join(l)
if result:
    print(result)
else:
    print('FRULA')