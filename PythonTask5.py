import tkinter as tk
from tkinter import ttk
import requests

# Function to get exchange rates
def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data['rates']

# Function to convert currency
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combobox.get()
        to_currency = to_currency_combobox.get()
        rates = get_exchange_rates()
        converted_amount = amount * rates[to_currency] / rates[from_currency]
        show_result(amount, from_currency, converted_amount, to_currency)
    except ValueError:
        result_label.config(text="Please enter a valid amount.")
    except KeyError:
        result_label.config(text="Currency not supported.")

# Function to show result in a new window
def show_result(amount, from_currency, converted_amount, to_currency):
    result_window = tk.Toplevel(window)
    result_window.title("Conversion Result")
    result_window.geometry("300x100")
    result_label = tk.Label(result_window, text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    result_label.pack(pady=20)

# Main window
window = tk.Tk()
window.title("Currency Converter")
window.geometry("400x300")

# Amount entry
amount_label = tk.Label(window, text="Amount in USD:")
amount_label.pack(pady=10)
amount_entry = tk.Entry(window)
amount_entry.pack(pady=5)

# From currency combobox
from_currency_label = tk.Label(window, text="From Currency:")
from_currency_label.pack(pady=10)
from_currency_combobox = ttk.Combobox(window, values=["USD"])
from_currency_combobox.set("USD")
from_currency_combobox.pack(pady=5)

# To currency combobox
to_currency_label = tk.Label(window, text="To Currency:")
to_currency_label.pack(pady=10)
to_currency_combobox = ttk.Combobox(window, values=list(get_exchange_rates().keys()))
to_currency_combobox.pack(pady=5)

# Convert button
convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack(pady=20)

# Result label
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()
