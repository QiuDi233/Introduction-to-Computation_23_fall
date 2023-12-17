word=input()
if word[-2:]=='er' or word[-2:]=='ly':
    word=word[:-2]

elif word[-3:]=='ing':
    word=word[:-3]
print(word)