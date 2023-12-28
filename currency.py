import tkinter as tk
from tkinter import ttk

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        # Dictionary of fixed exchange rates
        self.exchange_rates = {
            'USD': 1.0,
            'EUR': 0.92,
            'GBP': 0.75,
            'JPY': 110.0,
            'AUD': 1.35,
            'CAD': 1.25,
            'CHF': 0.92,
            'CNY': 6.46,
            'INR': 74.50,
            'MXN': 20.15,
            'NZD': 1.45,
            'SEK': 8.55,
            'SGD': 1.32,
            'ZAR': 15.10,
            'RUB': 72.80
        }

        # Variables
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.amount_var = tk.DoubleVar()

        # GUI elements
        ttk.Label(root, text="From Currency:").grid(row=0, column=0, padx=10, pady=10)
        from_currency_combobox = ttk.Combobox(root, textvariable=self.from_currency_var, values=list(self.exchange_rates.keys()))
        from_currency_combobox.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(root, text="To Currency:").grid(row=1, column=0, padx=10, pady=10)
        to_currency_combobox = ttk.Combobox(root, textvariable=self.to_currency_var, values=list(self.exchange_rates.keys()))
        to_currency_combobox.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(root, text="Amount:").grid(row=2, column=0, padx=10, pady=10)
        amount_entry = ttk.Entry(root, textvariable=self.amount_var)
        amount_entry.grid(row=2, column=1, padx=10, pady=10)

        convert_button = ttk.Button(root, text="Convert", command=self.convert_currency)
        convert_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def convert_currency(self):
        try:
            amount = float(self.amount_var.get())
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()

            # Perform conversion using fixed exchange rates
            result = amount * (self.exchange_rates[to_currency] / self.exchange_rates[from_currency])

            # Display the result
            self.result_label.config(text=f"Converted Amount: {result:.2f} {to_currency}")
        except ValueError:
            self.result_label.config(text="Please enter a valid amount.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()

