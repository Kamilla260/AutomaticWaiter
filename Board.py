from tkinter import *

window = Tk()
window.title('Automatic Waiter')

board = []

for i in range(0, 18):
    board.append([])
    for n in range(0, 32):
        if i == 0 and n == 31:
            color = '#190655'
        elif (n+i)%2 == 0:
            color = '#f3e6cb'
        else:
            color = '#dad8d4'
        newCanvas = Canvas(window, width=30, height=30, background=color)
        board[i].append(newCanvas)
        board[i][n].grid(row = i, column = n)
        newCanvas["highlightthickness"] = 0

window.mainloop()