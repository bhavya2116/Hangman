import random
def hangman():
    list_of_words=["bhavya","pandu"]
    word=random.choice(list_of_words)
    print(word)
    turns=10
    guessmade=''
    valid_entry=set("abcdefghijklmnopqrstuvwxyz")
    # print(valid_entry)
    # print(guessmade)
    while len(word)>0:
        mainword=""
        for letters in word:
            if letters in guessmade:
                mainword=mainword+letters
            else:
                mainword=mainword+"_ "
        if mainword==word:
            print(mainword)
            print(name,"you won the game!!!!")
            break
        print("guess the words",mainword)
        guess=input("guess word")
        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            ("enter a valid character")
        if guess not in word:
            turns=turns-1
            if turns==9:
                print("9 turns left!!!")
                print("-----------------")
            if turns==8:
                print("8 turns left!!!")
                print("-----------------")
                print("        0          ")
            if turns==7:
                print("7 turns left!!!")
                print("------------------")
                print("         0             ")
                print("         |             ")
            if turns==6:
                print("6 turns left!!!")
                print("------------------")
                print("         0             ")
                print("         |             ")
                print("        /             ")
            if turns==5:
                print("5 turns left!!!")
                print("------------------")
                print("         0             ")
                print("         |             ")
                print("        / \            ")
            if turns==4:
                print("4 turns left !!!")
                print("------------------")
                print("          0             ")
                print("         /|             ")
                print("         / \            ")
            if turns==3:
                print("3 turns left!!!")
                print("------------------")
                print("         0           ")
                print("        /|\             ")
                print("        / \            ")
            if turns==2:
                print("2 turns left!!!")
                print("------------------")
                print("        \0/ |          ")
                print("         |             ")
                print("        / \            ")
            if turns==1:
                print("only one turn left!!!")
                print("------------------")
                print("        \0/_|          ")
                print("         |             ")
                print("        / \            ")
            if turns==0:
                print("you loose")
                print("ypu let a good man die")
                print("------------------")
                print("        0_|          ")
                print("       /|\             ")
                print("       / \            ")
                break
name=input("enter a name::")
print("welcome",name,"!")
print("----------------------")
print("try to the guess the lessthan 10 attempts")
hangman()