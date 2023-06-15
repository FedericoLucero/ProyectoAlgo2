from tkinter import ttk
import tkinter as tk
  
# Creating the tkinter window
def exec(cars,personName,monto):
    print(cars)
    root = tk.Tk()
    root.title("Aceptar el viaje")
    text_label = ttk.Label(root, text="Persona "+personName+" con monto "+str(monto))
    text_label.pack(pady=10,anchor = tk.W )
    text_label2 = ttk.Label(root, text= "Estos son los vehiculos disponibles")
    text_label2.pack(pady=10, padx=1,anchor = tk.W )
    frame = tk.Frame(root)
    frame.pack(pady=10,anchor = tk.W)
    
    # Function for closing window
    var = tk.IntVar()
    var.set(1)
    if len(cars)>=1:
        R1 = ttk.Radiobutton(frame, text="Vehiculo "+cars[0][0]+" con valor: "+str(cars[0][1]), variable=var, value=1)
        R1.pack( anchor = tk.W,pady=1 )
    if len(cars)>=2:
        R2 = ttk.Radiobutton(frame, text="Vehiculo "+cars[1][0]+" con valor: "+str(cars[1][1]), variable=var, value=2)
        R2.pack( anchor = tk.W,pady=1 )
    if len(cars)>=3:
        R3 = ttk.Radiobutton(frame, text="Vehiculo "+cars[2][0]+" con valor: "+str(cars[2][1]), variable=var, value=3)
        R3.pack( anchor = tk.W,pady=1)
    
    def Close():
        root.destroy()
    def ReturnNone():
        var.set(0) 
        root.destroy()
                
    button_frame = ttk.Frame(root)
    button_frame.pack()
    # Button for closing
    accept_button = ttk.Button(button_frame, text="Aceptar viaje", command=Close)
    accept_button.pack(side=tk.RIGHT)
    exit_button = ttk.Button(button_frame, text="Rechazar viaje", command=ReturnNone)
    exit_button.pack(side=tk.LEFT)
    
    root.geometry("")
    root.mainloop()
    return var.get()


 