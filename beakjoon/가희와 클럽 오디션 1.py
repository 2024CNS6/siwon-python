lv, judgement = input().split()
lv = int(lv)
if judgement == 'miss':
    score = 0
elif judgement == 'bad':
    score = 200 * lv
elif judgement == 'cool':
    score = 400 * lv
elif judgement == 'great':
    score = 600 * lv
elif judgement == 'perfect':
    score = 1000 * lv
print(score)
