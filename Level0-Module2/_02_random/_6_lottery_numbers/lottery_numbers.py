import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    lotteryNum = ""
    # TODO 1) Get 6 random numbers to put on your lottery ticket
    for i in range(6):
        randNum = random.randint(1, 100)
        lotteryNum += str(randNum) + ", " #NEED TO TEACH STRING CONVERSION FIRST???

    # TODO 2) Display the selected numbers to the user in a pop-up

    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
    messagebox.showinfo("Winning Lottery Ticket", lotteryNum)
