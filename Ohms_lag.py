import tkinter as tk
from tkinter import ttk

def berakna():
    val = combo.get()
    try:
        if val == "Spänning (U)":
            I = float(entry1.get())
            R = float(entry2.get())
            U = I * R
            resultat.set(f"Spänningen (U) är {U:.2f} V")
        elif val == "Ström (I)":
            U = float(entry1.get())
            R = float(entry2.get())
            I = U / R
            resultat.set(f"Strömmen (I) är {I:.2f} A")
        elif val == "Resistans (R)":
            U = float(entry1.get())
            I = float(entry2.get())
            R = U / I
            resultat.set(f"Resistansen (R) är {R:.2f} Ω")
        elif val == "Effekt (P)":
            U = float(entry1.get())
            I = float(entry2.get())
            P = U * I
            resultat.set(f"Effekten (P) är {P:.2f} W")
    except Exception:
        resultat.set("Felaktig inmatning!")

def uppdatera_falt(event):
    val = combo.get()
    if val == "Spänning (U)":
        label1.config(text="Ström (I) i A:")
        label2.config(text="Resistans (R) i Ω:")
    elif val == "Ström (I)":
        label1.config(text="Spänning (U) i V:")
        label2.config(text="Resistans (R) i Ω:")
    elif val == "Resistans (R)":
        label1.config(text="Spänning (U) i V:")
        label2.config(text="Ström (I) i A:")
    elif val == "Effekt (P)":
        label1.config(text="Spänning (U) i V:")
        label2.config(text="Ström (I) i A:")
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    resultat.set("")

root = tk.Tk()
root.title("Ohms lag & Effekt")

ttk.Label(root, text="Vad vill du räkna ut?").grid(column=0, row=0, columnspan=2, pady=5)

combo = ttk.Combobox(root, values=["Spänning (U)", "Ström (I)", "Resistans (R)", "Effekt (P)"])
combo.current(0)
combo.grid(column=0, row=1, columnspan=2)
combo.bind("<<ComboboxSelected>>", uppdatera_falt)

label1 = ttk.Label(root, text="Ström (I) i A:")
label1.grid(column=0, row=2, sticky="e")
entry1 = ttk.Entry(root)
entry1.grid(column=1, row=2)

label2 = ttk.Label(root, text="Resistans (R) i Ω:")
label2.grid(column=0, row=3, sticky="e")
entry2 = ttk.Entry(root)
entry2.grid(column=1, row=3)

ttk.Button(root, text="Beräkna", command=berakna).grid(column=0, row=4, columnspan=2, pady=5)

resultat = tk.StringVar()
ttk.Label(root, textvariable=resultat).grid(column=0, row=5, columnspan=2, pady=5)

root.mainloop()