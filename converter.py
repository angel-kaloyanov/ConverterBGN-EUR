import tkinter as tk
from tkinter import messagebox, ttk

EUR_RATE = 1.95583


def calculate_change():
    try:
        # Вземане на стойностите от полетата
        purchase_value = float(entry_price.get())
        money_given = float(entry_paid.get())

        # Вземане на избраните валути
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

        # Изчисляваме рестото (лева)
        change_bgn = paid_in_bgn - price_in_bgn

        if change_bgn < 0:
            messagebox.showwarning("Грешка", "Дадените пари са по-малко от цената!")
            return

        # Превръщаме рестото в евро
        change_eur = change_bgn / EUR_RATE

        # Показваме резултата
        label_res_bgn.config(text=f"{change_bgn:.2f} BGN")
        label_res_eur.config(text=f"{change_eur:.2f} EUR")

    except ValueError:
        messagebox.showerror("Грешка", "Моля, въведете валидни числа!")


# Създаване на прозореца
root = tk.Tk()
root.title("Валутен Калкулатор Ресто")
root.geometry("500x450")
root.resizable(False, False)

style = ttk.Style()
style.configure("TLabel", font=("Arial", 14))
style.configure("TButton", font=("Arial", 14, "bold"))

# Полета за въвеждане
frame = ttk.Frame(root, padding="50")
frame.pack(fill="both", expand=True)

# Стойност на покупка
ttk.Label(frame, text="Стойност на покупка:").grid(row=0, column=0, sticky="w", pady=5)
entry_price = ttk.Entry(frame)
entry_price.grid(row=0, column=1, pady=5)
combo_price_curr = ttk.Combobox(frame, values=["BGN", "EUR"], width=5, state="readonly")
combo_price_curr.current(0)
combo_price_curr.grid(row=0, column=2, padx=5)

# Дадени пари
ttk.Label(frame, text="Пари от клиент:").grid(row=1, column=0, sticky="w", pady=5)
entry_paid = ttk.Entry(frame)
entry_paid.grid(row=1, column=1, pady=5)
combo_paid_curr = ttk.Combobox(frame, values=["BGN", "EUR"], width=5, state="readonly")
combo_paid_curr.current(0)
combo_paid_curr.grid(row=1, column=2, padx=5)

# Бутон за изчисление
btn_calc = ttk.Button(frame, text="ИЗЧИСЛИ РЕСТО", command=calculate_change)
btn_calc.grid(row=2, column=0, columnspan=3, pady=20)

# Резултати
ttk.Label(frame, text="Ресто в Лева:", font=("Arial", 14, "bold")).grid(row=3, column=0, sticky="w")
label_res_bgn = ttk.Label(frame, text="0.00 BGN", foreground="green", font=("Arial", 12, "bold"))
label_res_bgn.grid(row=3, column=1, sticky="w")

ttk.Label(frame, text="Ресто в Евро:", font=("Arial", 14, "bold")).grid(row=4, column=0, sticky="w")
label_res_eur = ttk.Label(frame, text="0.00 EUR", foreground="blue", font=("Arial", 12, "bold"))
label_res_eur.grid(row=4, column=1, sticky="w")

root.mainloop()