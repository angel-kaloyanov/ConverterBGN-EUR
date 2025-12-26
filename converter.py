import tkinter as tk
from tkinter import messagebox, ttk

EUR_RATE = 1.95583


def calculate_change():
    try:
        purchase_value = float(entry_price.get())
        money_given = float(entry_paid.get())

        price_curr = combo_price_curr.get()
        paid_curr = combo_paid_curr.get()

        if price_curr == "EUR":
            price_in_bgn = purchase_value * EUR_RATE
        else:
            price_in_bgn = purchase_value

        if paid_curr == "EUR":
            paid_in_bgn = money_given * EUR_RATE
        else:
            paid_in_bgn = money_given

        change_bgn = paid_in_bgn - price_in_bgn

        if change_bgn < 0:
            messagebox.showwarning("Грешка", "Дадените пари са по-малко от цената!")
            return

        change_eur = change_bgn / EUR_RATE

        label_res_bgn.config(text=f"{change_bgn:.2f} BGN")
        label_res_eur.config(text=f"{change_eur:.2f} EUR")

    except ValueError:
        messagebox.showerror("Грешка", "Моля, въведете валидни числа!")


FONT_LABEL = ("Arial", 14)
FONT_ENTRY = ("Arial", 14)
FONT_BUTTON = ("Arial", 14, "bold")
FONT_RESULT = ("Arial", 16, "bold")

root = tk.Tk()
root.title("Валутен Калкулатор")
root.geometry("550x450")
root.resizable(False, False)

style = ttk.Style()
style.configure("TLabel", font=FONT_LABEL)
style.configure("TButton", font=FONT_BUTTON)
style.configure("TCombobox", font=FONT_ENTRY)

frame = ttk.Frame(root, padding="30")
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Стойност на покупка:").grid(row=0, column=0, sticky="w", pady=10)
entry_price = ttk.Entry(frame, font=FONT_ENTRY, width=15)  # Директно задаваме шрифт тук
entry_price.grid(row=0, column=1, pady=10, padx=5)
combo_price_curr = ttk.Combobox(frame, values=["BGN", "EUR"], width=5, state="readonly", font=FONT_ENTRY)
combo_price_curr.current(0)
combo_price_curr.grid(row=0, column=2, padx=5)

ttk.Label(frame, text="Пари от клиент:").grid(row=1, column=0, sticky="w", pady=10)
entry_paid = ttk.Entry(frame, font=FONT_ENTRY, width=15)  # Директно задаваме шрифт тук
entry_paid.grid(row=1, column=1, pady=10, padx=5)
combo_paid_curr = ttk.Combobox(frame, values=["BGN", "EUR"], width=5, state="readonly", font=FONT_ENTRY)
combo_paid_curr.current(0)
combo_paid_curr.grid(row=1, column=2, padx=5)

btn_calc = ttk.Button(frame, text="ИЗЧИСЛИ РЕСТО", command=calculate_change)
btn_calc.grid(row=2, column=0, columnspan=3, pady=30, ipady=10, sticky="ew")

# Резултати
ttk.Label(frame, text="Ресто в Лева:", font=FONT_LABEL).grid(row=3, column=0, sticky="w", pady=5)
label_res_bgn = ttk.Label(frame, text="0.00 BGN", foreground="green", font=FONT_RESULT)
label_res_bgn.grid(row=3, column=1, columnspan=2, sticky="w", pady=5)

ttk.Label(frame, text="Ресто в Евро:", font=FONT_LABEL).grid(row=4, column=0, sticky="w", pady=5)
label_res_eur = ttk.Label(frame, text="0.00 EUR", foreground="blue", font=FONT_RESULT)
label_res_eur.grid(row=4, column=1, columnspan=2, sticky="w", pady=5)

root.mainloop()