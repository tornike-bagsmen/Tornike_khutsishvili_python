# დამუშავება - გააზრების პროცესშია 







# import requests
# from datetime import datetime

# def get_bitcoin_price_on_date(date):
#     url = f'https://api.coingecko.com/api/v3/coins/bitcoin/history'
#     params = {'date': date.strftime('%d-%m-%Y')}
#     response = requests.get(url, params=params)
#     data = response.json()
    
#     # Check if 'market_data' is in the response
#     if 'market_data' in data and 'current_price' in data['market_data'] and 'usd' in data['market_data']['current_price']:
#         return data['market_data']['current_price']['usd']
#     else:
#         raise ValueError("Could not fetch the Bitcoin price for the given date.")

# def main():
#     # User input
#     date_input = input("Enter the date when you bought Bitcoin (YYYY-MM-DD): ")
#     amount_bought = float(input("Enter the amount of Bitcoin you bought: "))
    
#     try:
#         # Convert date input to datetime object
#         bought_date = datetime.strptime(date_input, '%Y-%m-%d')
        
#         # Get Bitcoin price on the entered date
#         price_per_btc = get_bitcoin_price_on_date(bought_date)
#         total_spent = price_per_btc * amount_bought
        
#         print(f"On {bought_date.strftime('%Y-%m-%d')}, Bitcoin price was ${price_per_btc:.2f}")
#         print(f"You spent ${total_spent:.2f} to buy {amount_bought} Bitcoin.")
        
#         # Condition to win a car or lose an eye (for demonstration, we'll use a threshold of $10,000)
#         if total_spent > 10000:
#             print("Congratulations! You've won a car!")
#         else:
#             print("Better luck next time! You've lost an eye.")
    
#     except ValueError as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     main()