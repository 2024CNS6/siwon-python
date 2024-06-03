while True:
  try:
    base = int(input())
    if base == 0:
      break
    total_blocks = (base * base + base) // 2
    print(total_blocks)
  except ValueError:
    print("Invalid input: Please enter a positive integer.")