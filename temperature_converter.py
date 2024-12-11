import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = temp * 9/5 + 32
            elif to_unit == "Kelvin":
                result = temp + 273.15
            else:
                result = temp
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (temp - 32) * 5/9
            elif to_unit == "Kelvin":
                result = (temp - 32) * 5/9 + 273.15
            else:
                result = temp
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = temp - 273.15
            elif to_unit == "Fahrenheit":
                result = (temp - 273.15) * 9/5 + 32
            else:
                result = temp

        label_result.config(text=f"Converted: {result:.2f} {to_unit}")
    except ValueError:
        label_result.config(text="Invalid Input! Enter a number.")

app = tk.Tk()
app.title("Temperature Converter")
app.geometry("300x200")

tk.Label(app, text="Enter Temperature:").grid(row=0, column=0, pady=5)
entry_temp = tk.Entry(app)
entry_temp.grid(row=0, column=1, pady=5)

tk.Label(app, text="From Unit:").grid(row=1, column=0)
combo_from = ttk.Combobox(app, values=["Celsius", "Fahrenheit", "Kelvin"])
combo_from.grid(row=1, column=1)
combo_from.set("Celsius")

tk.Label(app, text="To Unit:").grid(row=2, column=0)
combo_to = ttk.Combobox(app, values=["Celsius", "Fahrenheit", "Kelvin"])
combo_to.grid(row=2, column=1)
combo_to.set("Fahrenheit")

tk.Button(app, text="Convert", command=convert_temperature).grid(row=3, column=0, columnspan=2, pady=10)
label_result = tk.Label(app, text="Converted: ")
label_result.grid(row=4, column=0, columnspan=2)

app.mainloop()
