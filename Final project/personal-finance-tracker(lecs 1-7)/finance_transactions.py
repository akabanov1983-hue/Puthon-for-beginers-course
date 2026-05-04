transactions = {
    1: {
        "type": "income",
        "amount": 3000.00,
        "category": "salary",
        "date": "2026-05-01",
        "comment": "Monthly salary"
    },
    2: {
        "type": "expense",
        "amount": 45.50,
        "category": "food",
        "date": "2026-05-01",
        "comment": "Lunch"
    }
}

def create_transaction():
    """Функция создает финансовую транзакцию"""

    transaction_id = max(transactions.keys()) + 1

    transaction_type = input("Введите категорию (доход/расход): ")
    amount = float(input("Введите сумму: "))
    category = input("Введите категорию: ")
    date =  input("Введите дату в формате гггг-мм-дд: ")
    comment = input("Введите комментарий: ")

    transactions[transaction_id] = {
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "date": date,
        "comment": comment
        }

    print(f'Транзакция успешно создана:\n'
          f'ID: {transaction_id}\n'
          f'Тип {transactions[transaction_id]["type"]}\n'
          f'Сумма: {transactions[transaction_id]["amount"]}\n'
          f'Категория: {transactions[transaction_id]["category"]}\n'
          f'Дата {transactions[transaction_id]["date"]}\n'
          f'Описание: {transactions[transaction_id]["comment"]}\n')



def get_transaction_by_id(transaction_id):
    """Функция возвращает транзакцию по ее идентификатору"""

    if transaction_id not in transactions.keys():
        print(f'Транзакции с идентификатором {transaction_id} не существует')

    else:
        print(f'ID: {transaction_id}\n'
              f'Тип {transactions[transaction_id]["type"]}\n'
              f'Сумма: {transactions[transaction_id]["amount"]}\n'
              f'Категория: {transactions[transaction_id]["category"]}\n'
              f'Дата {transactions[transaction_id]["date"]}\n'
              f'Описание: {transactions[transaction_id]["comment"]}\n')


def get_list_of_transactions():
    """Функция возвращает список всех транзакций"""

    for transaction_id in transactions.keys():
        print(f'transaction id: {transaction_id} |'
              f'type: {transactions[transaction_id]["type"]} |'
              f'amount: {transactions[transaction_id]["amount"]} |'
              f'category: {transactions[transaction_id]["category"]} |'
              f'date: {transactions[transaction_id]["date"]} |'
              f'comment: {transactions[transaction_id]["comment"]} |')



def delete_transaction_by_id(transaction_id):
    """Функция удаляет транзакцию по ее идентификатру"""

    if transaction_id not in transactions.keys():
        print(f'Транзакции с идентификатором {transaction_id} не существует')
    else:
        del transactions[transaction_id]
        print(f'Транзакция с идентификатором {transaction_id} успешно удалена')



def update_transaction_by_id(transaction_id):
    """Функция частично обновляет транзацкцию по ее идентификатору"""

    if transaction_id not in transactions.keys():
        print(f'Транзакция с идентификатором {transaction_id} не существует')
    else:
        print('Введите новое значение или "Enter" '
              'для пропуска и перехода к следующему')



# create_transaction()

# print(transactions)

# get_transaction_by_id(3)

# get_list_of_transactions()
#
# delete_transaction_by_id(1)
#
# get_list_of_transactions()
#
# delete_transaction_by_id(1)

