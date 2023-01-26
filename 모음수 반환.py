def count_vowels(word):
    cnt = 0
    for chr in word:
        if chr in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            cnt = cnt + 1
    return cnt

print(count_vowels('apple')) #=> 2
print(count_vowels('banana')) #=> 3        