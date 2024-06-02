# 변경된 알파벳 사전
croatian_alphabet_mapping = {
    "c-": "ć",
    "c=": "č",
    "d-": "dž",
    "d=": "đ",
    "l-": "lj",
    "l=": "lj",
    "n-": "nj",
    "n=": "nj",
    "s=": "ž",
}

# 입력 단어 읽기
word = input()

# 알파벳 개수 카운팅
alphabet_count = 0
for char in word:
    if char in croatian_alphabet_mapping:
        alphabet_count += 1
        continue

    # "dž", "lj", "nj", "š" 처리
    if char == "d" and word[word.index(char) + 1] == "ž":
        alphabet_count += 1
        continue
    elif char == "l" and (word[word.index(char) + 1] == "j" or word[word.index(char) + 1] == "n"):
        alphabet_count += 1
        continue
    elif char == "s" and word[word.index(char) + 1] == "š":
        alphabet_count += 1
        continue

    # 나머지 문자 처리
    alphabet_count += 2

# 크로아티아 알파벳 개수 출력
print(alphabet_count)
