from datetime import datetime

transactions = [
    {'date': '2023-01-05', 'amount': 100.0, 'description': 'Deposit'},
    {'date': '2023-01-12', 'amount': -50.5, 'description': 'Groceries'},
    {'date': '2023-02-15', 'amount': -1500.0, 'description': 'Rent'},
    {'date': '2023-02-18', 'amount': 20000.0, 'description': 'Bonus'},
    {'date': '2023-02-20', 'amount': -300.0, 'description': 'Utilities'}
]

result = {}

def total_balance(transactions):
    total_amount = 0
    for transaction in transactions:
        total_amount += transaction['amount']
    print(total_amount)
    return total_amount
def transactions_per_month(transactions):
    transactions_per_month = {}

    for transaction in transactions:
        date_obj = datetime.strptime(transaction['date'],'%Y-%m-%d')
        month_key = date_obj.strftime('%Y-%m')
        transactions_per_month[month_key] = transactions_per_month.get(month_key, 0 ) + 1
    print(transactions_per_month)
    return transactions_per_month
def average_debit(transactions):
    total_debit = 0
    count = 0
    for transaction in transactions:
        if transaction['amount'] < 0:
            total_debit += transaction['amount']
            count += 1
    total_debit /= count
    print(f"{total_debit:.2f}")
    return total_debit
def avarage_credit(transactions):
    total_credit = 0
    count = 0
    for transaction in transactions:
        if transaction['amount'] > 0:
            total_credit += transaction['amount']
            count += 1
    total_credit /= count
    print(f"{total_credit:.2f}")
    return total_credit

def months_with_highest_activity(transactions):
    ransactions_per_month = {}

    for transaction in transactions:
        date_obj = datetime.strptime(transaction['date'], '%Y-%m-%d')
        month_key = date_obj.strftime('%Y-%m')
        transactions_per_month[month_key] = ransactions_per_month.get(month_key, 0) + 1
        if ransactions_per_month


transactions_per_month(transactions)
total_balance(transactions)
average_debit(transactions)
avarage_credit(transactions)