import requests
import tkinter as tk
from tkinter import messagebox

def get_usd_rate():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Помилка заходу на сайт")

    data = response.json()
    return data[0]["rate"]

class CurrencyConverter:
    def __init__(self, rate):
        self.rate = rate

    def to_usd(self, amount_uah):
        return amount_uah / self.rate

def convert():
    try:
        amount = float(entry.get())
        result = converter.to_usd(amount)
        result_label.config(text=f"{result:.2f} USD")
    except ValueError:
        messagebox.showerror("Помилка", "Введіть число!")

try:
    rate = get_usd_rate()
    converter = CurrencyConverter(rate)
except Exception as e:
    print("Помилка при запуску:", e)
    exit()

root = tk.Tk()
root.title("Конвертер валют (UAH → USD)")
root.geometry("300x250")

title = tk.Label(root, text="Конвертер валют", font=("Arial", 14))
title.pack(pady=10)

another_label = tk.Label(root, text="Використовується офіційний курс НБУ")
another_label.pack(pady=10)

rate_label = tk.Label(root, text=f"Курс: {rate:.2f} грн")
rate_label.pack()

entry = tk.Entry(root)
entry.pack(pady=10)

convert_btn = tk.Button(root, text="Конвертувати", command=convert)
convert_btn.pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

author_label = tk.Label(root, text="Створено Андрієм", font=("Arial", 12))
author_label.pack()

root.mainloop()