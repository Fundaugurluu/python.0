import random
words=["python","pascal","java","swift","ruby","kotlin","go","assembly","matlab","dart","javascript","fortran","r","typescript","sql","php","c","html","css"]
def pick_word():
    return words[random.randint(0,len(words)-1)]

def check(word,guess):
    final=''
    wrong_place=''
    for i in range (len(word)):
        if word[i]==guess[i]:
            final+=word[i]
        elif guess[i] in word:
            if guess[i] not in wrong_place:
                if guess[i] not in final:
                    wrong_place+=guess[i]
            final+='*'
        else:
            final+='*'
    return final,wrong_place

def start_the_game():
    word=pick_word()
    final='*'*len(word)
    wrong_place=[]
    count=0
    while True:
        state=''
        if wrong_place:
            state="these are the letters that are'nt in the right place"+wrong_place
        count+=1
        print("the latest situation:",count,final,state)
        message="please guess a programming languge name of this length :{}   ".format(len(word))
        guess=input(message)
        if len(guess)!=len(word):
            print("the length of the word you gave is wrong")
            continue
        final,wrong_place=check(word,guess)
        if final==word:
            print("bravo! you have found the right word!".format(count))
            break

start_the_game()



    


