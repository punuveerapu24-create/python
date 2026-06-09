exchange_rates = {"USD": 1.0, "EUR": 0.92, "INR": 83.5, "JPY": 156.0}

base_amount = float(input("Enter the product base amount in USD: "))

target_currency = input("Enter your target currency code (e.g., 'INR'): ").upper()

conversion_rate = exchange_rates.get(target_currency)

if conversion_rate is not None:
    converted_amount = base_amount * conversion_rate
    print(f"{base_amount} USD = {converted_amount} {target_currency}")
else:
    print("Currency code profile not supported.")