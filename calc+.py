import tkinter as tk
from tkinter import*
from math import*

class Calc:
    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.title('Caculatrice')
        self.ecran = tk.Entry(self.fenetre, width= 35, borderwidth= 5)
        self.ecran.grid(row=0, column=0, columnspan= 6)
        self.boutons()
    
    def boutons(self):
        boutons= [
            '2nd','x!','√', '(', ')','%', '÷',
            'sin','cos','tan','7','8','9', '×',
            'ln','log','1/x','4','5','6','-',
            'exp','x^2','x^y','1','2','3','+',
            '|x|','Π','e','00','0','.','='
        ]
        row_val = 1
        col_val = 0

        for bouton in boutons:
            tk.Button(self.fenetre, text= bouton, width= 5, 
                    command= lambda bouton=bouton:
                    self.cliquer(bouton)).grid(row= row_val, column= col_val)
            col_val+=1
            if col_val > 6:
                col_val =0
                row_val +=1
        
        tk.Button(self.fenetre, text='C', width= 21,
                  command= self.effacer).grid(row=6, column=0, columnspan= 4)
        tk.Button(self.fenetre, text='Back', width= 10,
                  command= self.back).grid(row=6, column=4, columnspan= 4)
    
    def cliquer(self, bouton):
        if bouton == "=":
            try:
                result = eval(self.ecran.get())
                self.ecran.delete(0, tk.END)
                self.ecran.insert(tk.END, str(result))
            except Exception as e:
                self.ecran.delete(0, tk.END)
                self.ecran.insert(tk.END, 'Erreur')
        elif bouton == "×":
            self.ecran.insert(tk.END, "*")
        elif bouton == "÷":
            self.ecran.insert(tk.END, "/")
        elif bouton == "x^y":
            self.ecran.insert(tk.END, "**")
        elif bouton == "x^2":
            self.ecran.insert(tk.END, "**2")
        elif bouton == "sin":
            self.ecran.insert(tk.END, "sin(")
        elif bouton == "cos":
            self.ecran.insert(tk.END, "cos(")
        elif bouton == "tan":
            self.ecran.insert(tk.END, "tan(")
        elif bouton == "exp":
            self.ecran.insert(tk.END, "exp(")
        elif bouton == "ln":
            self.ecran.insert(tk.END, "log(")
        elif bouton == "log":
            self.ecran.insert(tk.END, "log10(")
        elif bouton == "√":
            self.ecran.insert(tk.END, "sqrt(")
        elif bouton == "|x|":
            self.ecran.insert(tk.END, "abs(")
        elif bouton == "Π":
            self.ecran.insert(tk.END, "pi")
        elif bouton == "%":
            self.ecran.insert(tk.END, "/100")
        elif bouton == "x!":
            self.ecran.insert(tk.END, "factorial(")
        else:
            self.ecran.insert(tk.END, bouton)
        

    def effacer(self):
        self.ecran.delete(0, tk.END)

    def back(self):
        index = self.ecran.get()
        self.ecran.delete(len(index)-1, tk.END)
        
    def run(self):
        self.fenetre.mainloop()

calculatrice = Calc()
calculatrice.run()