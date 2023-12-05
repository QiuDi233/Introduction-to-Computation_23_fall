letters=list(input())
n=int(input())
for i in range(n):
    word=input()
    f = True
    for letter in word:
        if letter not in letters:
            print("No")
            f= False
            break
        elif word.count(letter) > 1:
            if letter.count(letter) < word.count(letter):
                print(letter.count(letter) , word.count(letter))
                print("No")
                f= False
                break
    if f:
        print("Yes")
        for letter in word:
            letters.remove(letter)