import random, string
def hangman(word):
    wrong = 0
    stages = ["",
              "______      ",
              "|     |     ",
              "|     |     ",
              "|     o     ",
              "|    /|/    ",
              "|    //     ",
              "|           ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "１文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind =rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print(" あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print(" あなたの負け！正解は{}.".format(word))

def randomname(n):
   # randlst = [random.choice(string.digits) for i in range(n)]
   randlst = ["banana", "ringo", "momo"]
   return ''.join(randlst[])

while True:
    a = input(" 何文字？")
    a = int(a)
    hangman(randomname(a))
    ans = input(" 続ける？Yes:y, No:n")
    if ans == "n":
        break
    elif ans == "y":
        continue
    else:
        print(" ちゃんと読めあほ！！あばよっ！！")
        break
