import tkinter as tk
from tkinter import ttk, Frame, Canvas

#from tkinter import Frame, tk, Canvas
from random import choice

class Matrix(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.canvas= Canvas(master, bg='black')
        self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.velocidad = [i for i in range (0,30,5)]
        self.pos = [i for i in range (-200,200,20)]
        self.letters = []
        self.blue = 0
        self.caracteres = [
                    "あ", "い", "う", "え", "お", 
                    "か", "き", "く", "け", "こ",
                    "さ", "し", "す", "せ", "そ",
                    "た", "ち", "つ", "て", "と",
                    "な", "に", "ぬ", "ね", "の",
                    "は", "ひ", "ふ", "へ", "ほ",
                    "ま", "み", "む", "め", "も",
                    "や", "ゆ", "よ",
                    "ら", "り", "る", "れ", "ろ",
                    "わ", "を",
                    "ん",
                    "が", "ぎ", "ぐ", "げ", "ご",
                    "ざ", "じ", "ず", "ぜ", "ぞ",
                    "だ", "ぢ", "づ", "で", "ど",
                    "ば", "び", "ぶ", "べ", "ぼ",
                    "ぱ", "ぴ", "ぷ", "ぺ", "ぽ",
                ]
        self.draw()
        self.update()

    def draw(self):
        for x in range(0,1600,20):
            y = choice(self.pos)
            for j in range(0, choice([180,220,280]),20):
                self.obj = self.canvas.create_text(20+x, -200+y+j, text=choice(self.caracteres),
                    fill = 'blue2')
                self.letters.append(self.obj)

        def update(self):

            for letter in self.letters:
                v = choice(self.velocidad)    
                self.blue +=5
                color = '#{:02x}{:02x}{:02x}'.format(0,self.blue,0)
                self.canvas.itemconfig(letter, fill=color)
                self.canvas.move(letter,0,v)
                y = self.canvas.coords(self.obj)

                if self.blue >= 250:
                    self.blue = 0

            if y[1] >= 800:
                self.draw()
                
                if y[1] >= 1200:
                    self.letters.clear()
                    self.canvas.delete('all')

            self.canvas.after(80, self.update)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Matrix Legato')
    root.config(bg='black')
    #root.attributes('-fullscreen', True)
    app = Matrix(root)
    app.mainloop()