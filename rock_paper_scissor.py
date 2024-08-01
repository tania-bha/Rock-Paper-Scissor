import random
def game(round):
    for i in range(0,round):
        you=input("Rock or Paper or Scissor? ")
        print("You chose :" + you)
        radno=random.randint(1,3)
        if radno==1:
            comp='rock'
        elif radno==2:
            comp='paper'
        else:
            comp='scissor'
        print("Computer chose :" +comp)
        if(comp==you):
            print("SORRY!It's a tie")
        elif (comp=='r' and you=='p') or (comp=='s' and you=='r') or (comp=='p' and you=='s'):
            print("CONGRATS!You won.")
        else:
            print("OOPS!You loose")
    
round=int(input("How many rounds will be there?"))
print("there will be ", round, " rounds")
game(round)
