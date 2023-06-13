from tkinter import *
  
# Creating the tkinter window
def exec(cars):
    print(cars)
    root = Tk()
    root.geometry("200x120")
    
    # Function for closing window
    var = IntVar()
    def Close():
        root.destroy()
    if len(cars)>=1:
        R1 = Radiobutton(root, text="Auto "+cars[0][0]+". Valor: "+str(cars[0][1]), variable=var, value=1)
        R1.pack( anchor = W )

    if len(cars)>=2:
        R2 = Radiobutton(root, text="Auto "+cars[1][0]+". Valor: "+str(cars[1][1]), variable=var, value=2)
        R2.pack( anchor = W )
    if len(cars)>=3:
        R3 = Radiobutton(root, text="Auto "+cars[2][0]+". Valor: "+str(cars[2][1]), variable=var, value=3)
        R3.pack( anchor = W)
                
    # Button for closing
    exit_button = Button(root, text="aceptar", command=Close)
    exit_button.pack( anchor = W)
    
    root.mainloop()
    return var.get()
 