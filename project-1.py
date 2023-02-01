from random import randint as r
""" GUN WATER SANKE GAME RPOGRAM """

def game_win(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
print("COMP'S Turn: snakes(s) Water(w) gun(g) ")
randomno = r(1, 3)

if randomno == 1:
    comp = 's'
if randomno == 2:
    comp = 'w'
if randomno == 3:
    comp = 's'
#a=input(" comp player 1 turn : snakes(s) Water(w) gun(G)")
you = input("Your Turn :snakes(s) Water(w) gun(g)")
a = game_win(comp, you)
print(f"jarryas choose :{comp}")
print(f"you chooses {you}")
if a == None:
    print(" its the Tie !")
if a == True:
    print("you Win!!")
if a == False:
    print("You lose !")
