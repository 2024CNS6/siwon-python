arr = []
for _ in range(5):
  line = input()
  line = line.strip()
  arr.append(list(line))
result = ""
for j in range(15):
  column_chars = ""
  for i in range(5):
    if len(arr[i]) > j:
      column_chars += arr[i][j]
  result += column_chars
print(result)