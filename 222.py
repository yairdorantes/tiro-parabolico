import random
import tkinter as tk
import turtle
import math

from tkinter import Entry,Label, PhotoImage

G = 9.80665
origin_x = -780
origin_y = -180


#esta funcion es para guardar multimedia, esta si la saque de internet jaj
#homework = turtle.RawTurtle(canvas)
def resource_path(relative_path):

    try:

        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
path1=resource_path('ar.png')
def calculos(angulos,velocidad,tiempo):
    angulos = math.radians(angulos)
    x = velocidad * math.cos(angulos) * tiempo
    x = round(x,2)
    y = velocidad * math.sin(angulos) * tiempo

    w = -0.5*9.8*10**2

    res = y + w
    res = round(res,2)
    result['text'] = f'El objeto se encuentra a {x}m de distancia y a {res}m de altura a {tiempo} segundos de su lanzamiento'

    


def create_turtle():
    homework = turtle.RawTurtle(canvas)
    canvas.configure(bg='black')
    homework.shape('triangle')
    homework.hideturtle()
    homework.penup()
    homework.goto(origin_x, origin_y)
    homework.pendown()
   
    homework.left(45)
    homework.showturtle()
    homework.speed(1)

    return homework

def throw_turtle(turtle,angulo,power):
  

    for time in range(1, 25):
        x = power * math.cos(math.radians(angulo)) * time + origin_x
        y = power * math.sin(math.radians(angulo)) * time - (((time ** 2) * G) / 2) + origin_y
        
        turtle.goto(x, y)
        turtle.stamp()





def inciar():
        my_turtle = create_turtle()
        my_turtle.color(random.choice(['magenta', 'lightgreen', 'cyan', 'orangered', 'white']))
        throw_turtle(my_turtle,float(Wangulo.get()),float(Velocidad.get()))


raiz = tk.Tk()
raiz.title("TIRO PARABÓLICO")
canvas = tk.Canvas(master=raiz,width=2000,height=1500,background='black')

btnstart = tk.Button(
    master = raiz,
    text ="Calcular",
    bg='lightgreen',
    font=('bold',20),
    command=lambda: [
        calculos(float(Wangulo.get()),float(Velocidad.get()),float(tiempos.get())),
        inciar(),
        ])

btnstart.place(x=0,y=200)

canvas.grid(row=0, column=0, rowspan=10, columnspan=10) # , sticky='nsew')


angulo = Label(master=raiz, fg="black",bg='#4AC9C5', text="Ángulo: ",font=("bold",20))
angulo.place(x=0,y=0)


Wangulo = Entry(
    raiz,
    fg="blue",
    font=("bold", 15,)
)
Wangulo.place(x=120,y=0)

velo = Label(master=raiz, fg="black",bg='#4AC9C5', text="Velocidad(m/s): ",font=("bold",20))
velo.place(x=0,y=80)

Velocidad = Entry(
    raiz,
    fg="red",
    font=("bold", 15,)
)
Velocidad.place(x=250, y=80)



lbltiem = Label(master=raiz, fg="black",bg='#4AC9C5', text="Tiempo (s): ",font=("bold",20))

lbltiem.place(x=0,y=150)

tiempos = Entry(
    raiz,
    fg="green",
    font=("bold", 15,)
)

tiempos.place(x=180, y=150)

result = Label(master=raiz, fg="black",bg='#4AC9C5', text='',font=("bold",20))

result.place(x=0,y=250)

arrow = PhotoImage(file=path1)

arrow  = arrow.subsample(5,5)
lblarrow = Label(master=raiz, image=arrow)
lblarrow.place(x=135,y=910)

raiz.mainloop()

