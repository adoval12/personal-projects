#
# Alex Doval
# This is a program that allows you to play tower of Hanoi
# You can also use the program to veiw the fastest solution for a given tower of Hanoi
#
from myStack import *

"Tower of Hanoi Setup"
class TowerOfHanoi:
    def __init__(self, disks):
        self.tower1 = mystack()
        self.tower2 = mystack()
        self.tower3 = mystack()
        self.NumberOfDisks = disks
        self.move = 0
        n = disks
        for i in range(disks):
            self.tower1.push(n)
            n -= 1

    def moveDisk(self, t1, t2):
        if(t1.isEmpty() and t2.isEmpty()):
            print("both towers are empty. Please select a tower that has disk.")
        if(t1.isEmpty()):
            t1p = 0
        else:
            t1p = t1.peek()
        if(t2.isEmpty()):
            t2p = 0
        else:
            t2p = t2.peek()
        if( (t1p < t2p) or ((not t1.isEmpty()) and t2.isEmpty())):
            disk = t1.pop()
            t2.push(disk)
        else:
            print("cannot move disk")

    def choiceMoveDisk(self, t1, t2):
        if(t1 == 1 and t2 == 2):
            self.moveDisk(self.tower1, self.tower2)
        elif(t1 == 1 and t2 == 3):
            self.moveDisk(self.tower1, self.tower3)
        elif(t1 == 2 and t2 == 1):
            self.moveDisk(self.tower2, self.tower1)
        elif(t1 == 2 and t2 == 3):
            self.moveDisk(self.tower2, self.tower3)
        elif(t1 == 3 and t2 == 1):
            self.moveDisk(self.tower3, self.tower1)
        elif(t1 == 3 and t2 == 2):
            self.moveDisk(self.tower3, self.tower2)


    def solved(self):
        if (self.tower3.length() < self.NumberOfDisks):
            return False
        return True


    def solveTower(self,n,a,c,b):
        if n == 1:
            self.choiceMoveDisk(a,c)
            self.printTower(1)
            print()
        else:
            rn = n - 1
            self.solveTower(rn, a, b, c)
            self.choiceMoveDisk(a,c)
            self.printTower(1)
            print()
            self.solveTower(rn, b, c, a)

    def printTower(self, m):
        if m == 1:
            self.move += 1
            print()
            print("Move " + str(self.move))
            print()
        for i in range((self.NumberOfDisks),0,-1):
            l1 = self.tower1.length()
            l2 = self.tower2.length()
            l3 = self.tower3.length()
            n = i - 1
            if( i <= l1 and i <= l2 and i <= l3):
                print(" |" + str(self.tower1.stack[n]) + "|   |" + str(self.tower2.stack[n]) + "|   |" + str(self.tower3.stack[n]) + "|")
            elif(i <= l1 and i <= l2):
                print(" |" + str(self.tower1.stack[n]) + "|   |" + str(self.tower2.stack[n]) + "|   | |")
            elif(i <= l1 and i <= l3):
                print(" |" + str(self.tower1.stack[n]) + "|   | |   |" + str(self.tower3.stack[n]) + "|")
            elif(i <= l2 and i <= l3):
                print(" | |   |" + str(self.tower2.stack[n]) + "|   |" + str(self.tower3.stack[n]) + "|")
            elif(i <= l1):
                print(" |" + str(self.tower1.stack[n]) + "|   | |   | |")
            elif(i <= l2):
                print(" | |   |" + str(self.tower2.stack[n]) + "|   | |")
            elif(i <= l3):
                print(" | |   | |   |" + str(self.tower3.stack[n]) + "|")
            else:
                print(" | |   | |   | |")
        print(" ---   ---   ---")
        print(" |1|   |2|   |3|")

"This main function will allow the user to play the game"
def main():
    print("Hello!!!")
    print("Welcome to the Tower of Hanoi Game")
    disks = int(input("how many disks would you like "))
    print("here's your tower")
    print()
    while True:
        game = TowerOfHanoi(disks)
        game.printTower(0)
        print()
        print("Would you like to:")
        print("(1) solve it yourself")
        print("(2) veiw the fastest possible solution for your tower")
        print("(3) change the total number of disks ")
        print("(4) quit the program")
        choice = int(input("your choice: "))
        if choice == 1:
            print("you chose to solve it yourself")
            while(not(game.solved())):
                game.printTower(1)
                print()
                print("If you wish to exit, enter 4 for either as your first choice")
                c1 = int(input("select the tower of the disk you wish to move: "))
                if(c1 == 4):
                    print()
                    print("you exited to the main menu")
                    print()
                    break
                c2 = int(input("select the tower you wish to move your selected disk to: "))
                game.choiceMoveDisk(c1, c2)
                print("move was successful")
                print()
                if(game.solved()):
                    print()
                    game.printTower(0)
                    print()
                    print("CONGRATS!!!")
                    print("You solved the game!!")
                    print("It took a total of " + str(game.move) + " steps")
                    print()
        elif choice == 2:
            print("you chose to see the fastest solution")
            game.solveTower(disks,1,3,2)
            print("here is the fastest solution to this tower")
            print("It took a total of " + str(game.move) + " steps")
            print()
            EXIT = int(input("press any number to head back to the main menu"))
            print()
        elif choice == 3:
            print()
            disks = int(input("Enter a new number of disks"))
            print()
        elif choice == 4:
            print()
            print("you chose to quit")
            break
        else:
            print("invalid choice")
            print("please pick one of the options from 1 to 3")

main()


                
