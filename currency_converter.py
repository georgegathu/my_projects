from forex_python.converter import CurrencyRates

def get_exchange_rate(base_currency, target_currency):
    currency_rates = CurrencyRates()
    return currency_rates.get_rate(base_currency, target_currency)

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

def main():
    print("Welcome to Live Currency Converter!")

    african_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CNY', 'CAD', 'AUD', 'NZD', 'KSH']
    
    print("African Currencies:")
    for index, currency in enumerate(african_currencies, start=1):
        print(f"{index}. {currency}")
    
    try:
        base_currency_index = int(input("Select the base African currency (enter the corresponding number): "))
        if 1 <= base_currency_index <= len(african_currencies):
            base_currency = african_currencies[base_currency_index - 1]
        else:
            raise ValueError("Invalid selection.")
        
        target_currency = input("Enter the target currency code (e.g., USD): ").upper()
        
        exchange_rate = get_exchange_rate(base_currency, target_currency)
        print(f"Exchange rate from {base_currency} to {target_currency}: {exchange_rate}")
        
        amount = float(input(f"Enter the amount in {base_currency}: "))
        converted_amount = convert_currency(amount, exchange_rate)
        
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
