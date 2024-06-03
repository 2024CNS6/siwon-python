while True:
  try:
    N, S = map(int, input().split())
    x = S // (N + 1)
    print(x if x > 0 else 0)
  except EOFError:
    break