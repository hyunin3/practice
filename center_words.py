words = input()
def center(words):
    for chr in words:
        if len(words) % 2 == 0:
            return words[int(len(words)/2)], words[int(len(words)/2 + 1)]
        elif len(words) % 2 != 0:
            return words[int(len(words)//2 + 1)]
print(center(words))