import tkinter as tk
from tkinter import messagebox
import csv
import os

#Calculate

def calculate_bmi():
    try:
        name = name_entry.get().strip()

        if name == "":
            messagebox.showerror("Error", "Please enter your name.")
            return

        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and Height must be greater than 0.")
            return

        bmi = weight / ((height / 100) ** 2)

        if bmi < 18.5:
            category = "Underweight"
            advice = "Eat a healthy balanced diet."
        elif bmi < 25:
            category = "Normal"
            advice = "Keep maintaining your healthy lifestyle."
        elif bmi < 30:
            category = "Overweight"
            advice = "Exercise regularly and avoid junk food."
        else:
            category = "Obese"
            advice = "Consult a doctor and exercise regularly."

        bmi_value.config(text=f"{bmi:.2f}")
        category_value.config(text=category)
        advice_value.config(text=advice)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


#Save Record 

def save_record():

    if bmi_value["text"] == "--":
        messagebox.showwarning("Warning", "Calculate BMI first.")
        return

    file_exists = os.path.isfile("bmi_records.csv")

    with open("bmi_records.csv", "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Name", "Weight", "Height", "BMI", "Category"])

        writer.writerow([
            name_entry.get(),
            weight_entry.get(),
            height_entry.get(),
            bmi_value["text"],
            category_value["text"]
        ])

    messagebox.showinfo("Success", "Record saved successfully.")


#Clear

def clear():

    name_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

    bmi_value.config(text="--")
    category_value.config(text="--")
    advice_value.config(text="")


#GUI 

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("450x500")
root.resizable(False, False)

title = tk.Label(root, text="BMI Calculator",
                 font=("Arial", 20, "bold"))
title.pack(pady=15)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Name").grid(row=0, column=0, pady=5, sticky="w")
name_entry = tk.Entry(frame, width=25)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Weight (kg)").grid(row=1, column=0, pady=5, sticky="w")
weight_entry = tk.Entry(frame, width=25)
weight_entry.grid(row=1, column=1)

tk.Label(frame, text="Height (cm)").grid(row=2, column=0, pady=5, sticky="w")
height_entry = tk.Entry(frame, width=25)
height_entry.grid(row=2, column=1)

tk.Button(root,
          text="Calculate BMI",
          command=calculate_bmi,
          width=20,
          bg="green",
          fg="white").pack(pady=15)

result = tk.Frame(root)
result.pack()

tk.Label(result, text="BMI :").grid(row=0, column=0, sticky="w")
bmi_value = tk.Label(result, text="--")
bmi_value.grid(row=0, column=1)

tk.Label(result, text="Category :").grid(row=1, column=0, sticky="w")
category_value = tk.Label(result, text="--")
category_value.grid(row=1, column=1)

tk.Label(result, text="Advice :").grid(row=2, column=0, sticky="nw")
advice_value = tk.Label(result, text="", wraplength=250, justify="left")
advice_value.grid(row=2, column=1)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

tk.Button(button_frame,
          text="Save",
          width=10,
          command=save_record).grid(row=0, column=0, padx=5)

tk.Button(button_frame,
          text="Clear",
          width=10,
          command=clear).grid(row=0, column=1, padx=5)

tk.Button(button_frame,
          text="Exit",
          width=10,
          command=root.destroy).grid(row=0, column=2, padx=5)

root.mainloop()