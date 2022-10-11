import string
def minion_game(s):
    vowel=0
    const=0
    lis=list(s)
    for i in range(len(lis)):
        if lis[i] in "AEIOU":
            vowel=vowel+(len(lis)-i)
        else:
            const=const+(len(lis)-i)
    if const>vowel:
        print("Stuart",const)
    elif const==vowel:
        print("Draw")
    else:
        print("Kevin",vowel)

if __name__ == '__main__':
    s = input()
    minion_game(s)