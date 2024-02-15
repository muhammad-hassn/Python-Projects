# Build a program that can convert currency from one form to another using the latest
# exchange rates.

def currency_converter(amount, from_currency, to_currency):
    # Fetch the latest exchange rates from an API
    exchange_rates = get_exchange_rates()

    # Convert the amount from the source currency to USD
    usd_amount = amount / exchange_rates[from_currency]

    # Convert the USD amount to the target currency
    target_amount = usd_amount * exchange_rates[to_currency]

    return target_amount

def get_exchange_rates():
    # Fetch the latest exchange rates from an API
    # Replace this with the actual API call to get the exchange rates
    exchange_rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'GBP': 0.72,
        'JPY': 110.0,
        'CAD': 1.25,
        # Add more currencies and their exchange rates here
    }

    return exchange_rates

# Example usage
amount = 100
from_currency = 'USD'
to_currency = 'EUR'

converted_amount = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")

