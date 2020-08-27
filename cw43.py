from tkinter import *
def fun(r,c):
    global player
    if player=='X' and state[r][c]==0 and stopgame==False:
        player='O'
        list1[r][c].configure(text='X',fg='blue',bg='white')
        state[r][c]='X'
    elif player=='O' and state[r][c]==0 and stopgame==False:
        state[r][c]='O'
        player='X'
        list1[r][c].configure(text='O',fg='blue',bg='white')
    CheckforWin()
def CheckforWin():
    global stopgame
    for i in range(3):
        if state[i][0]==state[i][1]==state[i][2]!=0:
            list1[i][0].configure(bg='grey')
            list1[i][1].configure(bg='grey')
            list1[i][2].configure(bg='grey')
            stopgame=True
    for i in range(3):
        if state[0][i]==state[1][i]==state[2][i]!=0:
            stopgame=True
            list1[0][i].configure(bg='grey')
            list1[1][i].configure(bg='grey')
            list1[2][i].configure(bg='grey')
    if state[0][0]==state[1][1]==state[2][2]!=0:
        list1[0][0].configure(bg='grey')
        list1[1][1].configure(bg='grey')
        list1[2][2].configure(bg='grey')
        stopgame=True
    if state[2][0]==state[1][1]==state[0][2]!=0:
        stopgame=True
        list1[2][0].configure(bg='grey')
        list1[1][1].configure(bg='grey')
        list1[0][2].configure(bg='grey')
player='X'
root=Tk()
list1=[[0,0,0],[0,0,0],[0,0,0]]
state=[[0,0,0],[0,0,0],[0,0,0]]
stopgame=False
for i in range(3):
    for j in range(3):
        list1[i][j]=Button(width=3,font=('Verdana',56),bg='yellow',command=lambda r=i, c=j: fun(r,c))
        list1[i][j].grid(row=i,column=j)
mainloop()