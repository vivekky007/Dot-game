import tkinter as tk 
from tkinter import messagebox
import random as rn
import sys
import os
# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


main = tk.Tk()
main.title("The Dot game")
f2 = tk.Frame(main)
f1 = tk.Frame(main)

lab1 = tk.Label(f1,text = "welcome",font=("Georgia", 20))
lab1.place(x= 50,y = 80)
def des():
    f1.destroy()
main.after(2000,des)
lab2 = tk.Label(f2,text= "choose the size of the frame")
lab2.pack()


b1 = tk.StringVar(f2)
b1.set("choose")
drop = tk.OptionMenu(f2,b1,"Small","Medium","Large")
drop.pack()
b2 = tk.StringVar(f2)
b2.set("choose")

thresh=4
size=20
turn = 0
color = None
coloro = None
awin = False
#*******************************************************************************************************************************
#*******************************************************************************************************************************

def general_check_point(x,y,thresh,size):
    global xcor,ycor
    xd=x%size
    yd=y%size
    if xd<=thresh:
        x_corrected=x-xd
        if yd <=thresh:
            y_corrected=y-yd
        elif yd>=size-thresh:
            y_corrected=y-yd+size       
        else:                                                                       # CHECKED #
            return -1,-1
        
        

        return x_corrected,y_corrected

    elif xd>=size-thresh:
        x_corrected=x-xd+size
        if yd <=thresh:
            y_corrected=y-yd
        elif y>=size-thresh:
            y_corrected=y-yd+size
        else:
            return -1,-1

        return x_corrected,y_corrected
    else:
        return -1,-1
    return x_corrected,y_corrected
#*******************************************************************************************************************************
#*******************************************************************************************************************************

    
def check_point2(x1_corrected,y1_corrected,x2,y2,thresh,size):
    x2_corrected,y2_corrected=general_check_point(x2,y2,thresh,size)
    if y1_corrected==y2_corrected and x1_corrected==x2_corrected:
        return -1,-1
    else:
        squared_distance=(x1_corrected-x2_corrected)**2+(y1_corrected-y2_corrected)**2
        if squared_distance==size**2:
            return x2_corrected,y2_corrected
        else:
            return -1,-1
    

    

#*******************************************************************************************************************************
#*******************************************************************************************************************************
def player2(x1,y1,x2,y2,canvas,color):
    global xcor,ycor,points_recorded
    canvas.create_line(x1,y1,x2,y2,fill = color,width=3)
    xcor.clear()
    ycor.clear()
    points_recorded = 0

#*******************************************************************************************************************************
#*******************************************************************************************************************************
def player1(x1,y1,x2,y2,canvas,color):
    global xcor,ycor,points_recorded
    canvas.create_line(x1,y1,x2,y2,fill = color ,width=3)
    xcor.clear()
    ycor.clear()
    points_recorded = 0
#*******************************************************************************************************************************
#*******************************************************************************************************************************

def win(dd,canvas):
    global c,c2,uv1,uv2,dv1,dv2,pr1,pr2,points,awin
    X = (dd[0][0]+dd[0][1])/2
    Y = (dd[1][0]+dd[1][1])/2
    if dd[1][0] == dd[1][1] and line>=3:
    
        c = [[dd[0][0],dd[0][1]],[dd[1][0]+20,dd[1][1]+20]]
        dv1 = [[dd[0][0],dd[0][0]],[dd[1][0],c[1][0]]]
        dv2 = [[dd[0][1],dd[0][1]],[dd[1][1],c[1][0]]]
        c2 = [[dd[0][0],dd[0][1]],[dd[1][0]-20,dd[1][1]-20]]
        uv1 = [[dd[0][0],dd[0][0]],[dd[1][0],c2[1][0]]]
        uv2 = [[dd[0][1],dd[0][1]],[dd[1][1],c2[1][0]]]
        crev= [[dd[0][1], dd[0][0]], [dd[1][1] + 20, dd[1][0] + 20]]
        dv1rev = [[dd[0][0], dd[0][0]], [c[1][0], dd[1][0]]]
        dv2rev = [[dd[0][1], dd[0][1]], [c[1][0], dd[1][1]]]
        c2rev= [[dd[0][1], dd[0][0]], [dd[1][1] - 20, dd[1][0] - 20]]
        uv1rev = [[dd[0][0], dd[0][0]], [c2[1][0], dd[1][0]]]
        uv2rev = [[dd[0][1], dd[0][1]], [c2[1][0], dd[1][1]]]
        
        if (c in xy_cor_list or crev in xy_cor_list) and (dv1 in xy_cor_list or dv1rev in xy_cor_list) and (dv2 in xy_cor_list or dv2rev in xy_cor_list) and (c2 in xy_cor_list or c2rev in xy_cor_list) and (uv1 in xy_cor_list or uv1rev in xy_cor_list) and (uv2 in xy_cor_list or uv2rev in xy_cor_list):
            Y+=10
            canvas.create_oval(X-thresh,Y-thresh,X+thresh,Y+thresh,fill=coloro)                                                                
            Y-=20
            canvas.create_oval(X-thresh,Y-thresh,X+thresh,Y+thresh,fill=coloro)
            points = 2  
            awin = True      
        elif (c in xy_cor_list or crev in xy_cor_list) and (dv1 in xy_cor_list or dv1rev in xy_cor_list) and (dv2 in xy_cor_list or dv2rev in xy_cor_list):
            Y+=10
            canvas.create_oval(X-thresh,Y-thresh,X+thresh,Y+thresh,fill=coloro)
            points = 1
            awin = True 
        elif (c2 in xy_cor_list or c2rev in xy_cor_list) and (uv1 in xy_cor_list or uv1rev in xy_cor_list) and (uv2 in xy_cor_list or uv2rev in xy_cor_list):
            Y-=10
            canvas.create_oval(X-thresh,Y-thresh,X+thresh,Y+thresh,fill=coloro)
            points = 1
            awin = True 
        else:
            points = 0
            awin = False

    
    elif dd[0][0] == dd[0][1] and line>=3:
        c = [[dd[0][0]+20,dd[0][1]+20],[dd[1][0],dd[1][1]]]
        c2 = [[dd[0][0]-20,dd[0][1]-20],[dd[1][0],dd[1][1]]]
        dv1 = [[dd[0][0],c[0][0]],[dd[1][0],dd[1][0]]]
        dv2 = [[dd[0][1],c[0][1]],[dd[1][1],dd[1][1]]]
        uv1 = [[dd[0][0],c2[0][0]],[dd[1][0],dd[1][0]]]
        uv2 = [[dd[0][1],c2[0][1]],[dd[1][1],dd[1][1]]]
        crev = [[dd[0][1]+20, dd[0][0]+20], [dd[1][1], dd[1][0]]]
        c2rev = [[dd[0][1]-20, dd[0][0]-20], [dd[1][1], dd[1][0]]]
        dv1rev = [[crev[0][0], dd[0][0]], [dd[1][0], dd[1][0]]]
        dv2rev = [[crev[0][1], dd[0][1]], [dd[1][1], dd[1][1]]]
        uv1rev = [[c2rev[0][0], dd[0][0]], [dd[1][0], dd[1][0]]]
        uv2rev = [[c2rev[0][1], dd[0][1]], [dd[1][1], dd[1][1]]]
    
        if (c in xy_cor_list or crev in xy_cor_list) and (dv1 in xy_cor_list or dv1rev in xy_cor_list) and (dv2 in xy_cor_list or dv2rev in xy_cor_list) and (c2 in xy_cor_list or c2rev in xy_cor_list) and (uv1 in xy_cor_list or uv1rev in xy_cor_list) and (uv2 in xy_cor_list or uv2rev in xy_cor_list):
            X+=10
            canvas.create_oval(X-thresh,Y-thresh,X+thresh,Y+thresh,fill=coloro)
            X-=20
            canvas.create_oval(X-thresh,Y-thresh,X+thresh,Y+thresh,fill=coloro)
            
            points = 2
            awin = True   
        elif (c in xy_cor_list or crev in xy_cor_list) and (dv1 in xy_cor_list or dv1rev in xy_cor_list) and (dv2 in xy_cor_list or dv2rev in xy_cor_list):
            X+=10
            canvas.create_oval(X-thresh,Y-thresh,X+thresh,Y+thresh,fill=coloro)
            points = 1
            awin = True 
        elif (c2 in xy_cor_list or c2rev in xy_cor_list) and (uv1 in xy_cor_list or uv1rev in xy_cor_list) and (uv2 in xy_cor_list or uv2rev in xy_cor_list):
            X-=10
            canvas.create_oval(X-thresh,Y-thresh,X+thresh,Y+thresh,fill=coloro)
            points = 1
            awin = True 
        else:
            points = 0
            awin = False
    else:   
        print("ELSE BLOCK")

#*******************************************************************************************************************************
#*******************************************************************************************************************************

xcor = []
ycor = []
points_recorded = 0
xy_cor_list = []
corp1 = []
corp2 = []
line = 0
pred = 0
pgreen = 0

def resize():
    global x, y, bor, fsize, mar, text, ymar,xt,yt,fontl
    size = b1.get()
    if size == "Small":
        x = 300
        y = 300
        bor = 50
        fsize = 10
        mar = 20
        ymar = 25
        fontl = 20
        xt = 70
        yt = (y/2)-30
        main.geometry(f"{x}x{y}")
        start()
        f2.destroy()
    if size == "Medium":
        x = 600
        y = 600
        bor = 90
        ymar = 40
        fsize = 16
        mar = 35
        fontl = 46
        xt = (x/2)-200
        yt = (y/2)-100
        main.geometry(f"{x}x{y}")
        start()
        f2.destroy()
    if size == "Large":
        x = 900
        y = 900
        bor = 150
        ymar= 70
        fsize = 20
        mar = 40
        fontl = 46
        xt = (x/2)-210
        yt = (y/2)-100
        main.geometry(f"{x}x{y}")
        start()
        f2.destroy()
resize()
def evaluate():
    global fsize
    if pgreen>pred:
        text1 = "player1 wins!!"

        
    elif pgreen<pred:
        text1 = "player2 wins!!"

    else:
        text1 = "match tied"

    win_lab = tk.Label(main,text = text1,font=("Helvetica", fontl))
    win_lab.place(x = xt,y = yt)
    def desm():
        main.destroy()
    main.after(2000,desm)

def show():
        p1 = tk.Label(main, text=f"Player1 : {pgreen}", font=("Helvetica", fsize))
        p1.place(x=10, y=(y - bor) + 10)
        p2 = tk.Label(main, text=f"Player2 : {pred}", font=("Helvetica", fsize))
        p2.place(x=10, y=(y - bor) + 10+mar)  
        exit_button = tk.Button(main,text = "Exit",command=evaluate)
        exit_button.place(x = x-100,y = (y-ymar))   

    


def start():
    canvas = tk.Canvas(main,width = x,height= y-bor)
    
    dot_spacing = 20
    for i in range(-x, x, dot_spacing):
        for j in range(-y, y, dot_spacing):
            canvas.create_oval(i - 2, j - 2, i + 2, j + 2, fill="black") 
    canvas.pack()
    show()
    def on_canvas_click(event):
        global points_recorded,thresh,turn,size,xy_cor_list,color,coloro,line,pred,pgreen,points,awin
        print("canvas",turn)
    
        points = 0
        x1 = event.x
        y1 = event.y
        print("****************************************************")
        print(f"###############      TURN:{turn}      ################")
        if turn == 0 :

            if points_recorded==0:
                
                coloro = "green"
                a,b=general_check_point(x1,y1,thresh,size)
                if a==-1:
                    return
                xcor.append(a)
                ycor.append(b)
                points_recorded += 1
                canvas.create_oval(a-thresh,b-thresh,a+thresh,b+thresh,fill=coloro)
            elif points_recorded==1:
                color = "green"
                a,b=check_point2(xcor[0],ycor[0],x1,y1,thresh,size)
                if a==-1:
                    return
                xcor.append(a)
                ycor.append(b)
                dd = [list(xcor), list(ycor)]
                
                r0 = list(reversed(dd[0]))
                r1 = list(reversed(dd[1]))
                rev = [r0,r1]

                found_match = False

                for i in range(len(xy_cor_list)):
                    if (dd == xy_cor_list[i])  or (rev == xy_cor_list[i]):
                        messagebox.showerror("Error","can't choose already selected points")
                        if (dd in corp2) or (rev in corp2):
                            points_recorded = 1
                            color = "red"
                            coloro = "red"
                            aa = dd[0][0]
                            bb = dd[1][0]
                            canvas.create_oval(aa-thresh,bb-thresh,aa+thresh,bb+thresh,fill="red")
                            
                            
                            
                        else:
                            pass
                        

                        found_match = True
                        


                        

                if not found_match:
                    xy_cor_list.append(dd)
                    corp1.append(dd)
                    line+=1
                    win(dd,canvas)
                    pgreen = pgreen+points
                    show()
                    


               
                if found_match == True:
                    points_recorded += 0
                    canvas.create_oval(a-thresh,b-thresh,a+thresh,b+thresh,fill=coloro)
                    player2(xcor[0],ycor[0],xcor[1],ycor[1],canvas,color)
                    turn += 0
                else:
                    points_recorded += 1
                    canvas.create_oval(a-thresh,b-thresh,a+thresh,b+thresh,fill=coloro)
                    player2(xcor[0],ycor[0],xcor[1],ycor[1],canvas,color)
                    if(awin == True):
                        turn = turn + 0
                    else:
                        turn = turn + 1
            

                
        elif turn == 1:

            if points_recorded==0:
                coloro = "red"
                a,b=general_check_point(x1,y1,thresh,size)
                if a==-1:
                    return
                xcor.append(a)
                ycor.append(b)
                points_recorded += 1
                canvas.create_oval(a-thresh,b-thresh,a+thresh,b+thresh,fill=coloro)
            elif points_recorded==1:
                color = "red"
                a,b=check_point2(xcor[0],ycor[0],x1,y1,thresh,size)
                if a==-1:
                    return
                xcor.append(a)
                ycor.append(b)
                dd = [list(xcor), list(ycor)]
                r0 = list(reversed(dd[0]))
                r1 = list(reversed(dd[1]))
                rev = [r0,r1]

                found_match = False

                for i in range(len(xy_cor_list)):
                    if (dd == xy_cor_list[i]) or (rev == xy_cor_list[i]):
                        messagebox.showerror("Error","Can't choose already selected points")
                        if (dd in corp1) or (rev in corp1):
                            color = "green"
                            coloro = "green"
                            aa = dd[0][0]
                            bb = dd[1][0]
                            canvas.create_oval(aa-thresh,bb-thresh,aa+thresh,bb+thresh,fill="green")
                            
                        else:
                            pass
                        found_match = True
                        



                if not found_match:
                    xy_cor_list.append(dd)
                    corp2.append(dd)
                    line+=1
                    win(dd,canvas)
                    pred = pred+points
                    show()
                if found_match == True:
                    points_recorded +=0
                    canvas.create_oval(a-thresh,b-thresh,a+thresh,b+thresh,fill=coloro)
                    player1(xcor[0],ycor[0],xcor[1],ycor[1],canvas,color)
                    turn+=0
                else:
                    points_recorded += 1
                    canvas.create_oval(a-thresh,b-thresh,a+thresh,b+thresh,fill=coloro)
                    player1(xcor[0],ycor[0],xcor[1],ycor[1],canvas,color)
                    if(awin == True):
                        turn = turn + 0
                    else:
                        turn = turn - 1




   
    canvas.bind("<Button-1>", on_canvas_click)

b1.trace_add("write", lambda *args: resize()) 
f1.place(x = 0,y = 0 , relheight=1,relwidth=1)
f2.place(x = 0,y = 0 , relheight=1,relwidth=1)
main.mainloop()
