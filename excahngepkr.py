import requests

def get_current_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    data = response.json()

    if data.get("result") == "success":
        rate = data.get("conversion_rate")
        if rate is not None:
            return rate
        else:
            return "Conversion rate not found in response."
    else:
        return "Error fetching data from the API: " + data.get("error_type", "Unknown error")

# Use your provided API key
api_key = '2615ea2686bba75356bb7d32'

# Set the base and target currencies
base_currency = 'PLN'
target_currency = 'PKR'

# Get the current exchange rate
exchange_rate = get_current_exchange_rate(api_key, base_currency, target_currency)
print(f"Current Exchange Rate from {base_currency} to {target_currency}: {exchange_rate}")
