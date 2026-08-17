def calculate_cashback(amount, cashback_rate=0.05):
    cashback_amount = amount * cashback_rate
    return cashback_amount

zomoto_cashback = calculate_cashback(500)

print("Zomoto Cashback :", zomoto_cashback)

flipcart_cashback = calculate_cashback(2000,0.07)

print("Fliptcart Cashback :", flipcart_cashback)