import word_generate as w
print("WELCOME TO THE HANGMAN GAME!!!!!!!!\nTRY TO GUESS THE WORD BY TRYING TO GUESS THE CHARACTERS PRESENT IN IT ONE AT A TIME!!!!!\nIF YOU DO NOT GUESS CORRECTLY BEFORE THE MAN IS HANGED YOU LOSE!!!")
print("Best of luck!!!")
tries=7
word=w.gen()
s="_"*len(word)
print(s)
hang = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

t=0
f=0
while(tries!=0):
    x=input("Guess a character which may be in the word: ")
    if x in word:
        l=word.count(x)
        ind=0
        for i in range(l):
            if i==0:
                ind=word.find(str(x))
            else:
                ind=word.find(str(x),ind)
            s=s[0:ind]+x+s[ind+1:len(word)]
        print("\n",x,"is present in the word!!!You are going good!!!")
        print(s)
    else:
        print("This character is not present in the word!!!! Try another character!!!!")
        tries=tries-1
        print("Number of tries remaining:",tries)
        print(hang[t])
        t=t+1
    if s==word:
        f=1
        break

if f==1:
    print("Congratulations: You won!!!!")
else:
    print("Better luck next time!!!!!")
    print("The word was :",word)







    































