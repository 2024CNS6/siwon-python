import sys
input = sys.stdin.read()
a = map(int, input.replace('\n', '').split(','))
print(sum(a))