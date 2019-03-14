# -*- coding: utf-8 -*-

import random

def hangman(word):
    wrong = 0
    stages = ["",
    "_________     ",
    "|             ",
    "|      　|     ",
    "|      　O     ",
    "|      ／|＼   ",
    "|      ／ ＼   ",
    "|             "
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\r\n")
        print(" ".join(board))
        msg = "1文字を予想してね(" + str(len(stages)-wrong-1) + "/" + str(len(stages)-1) + "):"
        char = input(msg)
        if char in rletters:
            while char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
        else:
            wrong += 1
# print(" ".join(board))
        e = wrong + 1
    
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))


wordlists = ["cat","dog","paper","sandwitch","butter","soap","powder","salt","finger"]

hangman(wordlists[random.randint(0,len(wordlists))])

