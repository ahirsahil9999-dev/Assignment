# Build a generator function called cashback_generator(transactions) 
# that takes a list of Paytm transaction amounts and yields 5% cashback
# for each transaction. Print out the cashback values for all transactions.

def cashback_generator(transactions):
    for amount in transactions:
        result = amount * 0.05
        yield result
        
transactions = list(map(int, input("Enter Your Transaction :").split()))

result = cashback_generator(transactions)

for value in result:
    print("CashBack: ", value)