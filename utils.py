from datetime import datetime

transactions:dict[str,list[dict[str,str|int]]] = {}

def validate_date(date: str):
  try:
    if date != datetime.strptime(date,"%Y-%m-%d").strftime("%Y-%m-%d"):
      raise ValueError
    return True
  except ValueError:
    return False

def print_category(category:str, categoryExists:list[dict[str, str | int]]):
  print("\nCategory:", category)
  print()
  print("Date        Amount    Description")
  print("-----------------------------------")

  for item in categoryExists:
      print(
          item.get("date"),
          "\t",
          item.get("amount"),
          "\t",
          item.get("description")
      )

def total_expenses():
  """Return dict with category totals"""

  total_amount = 0
  category_transactions = transactions.values()

  for transaction_list in category_transactions:
    for transaction in transaction_list:
      transaction_amount = transaction.get("amount")
      if isinstance(transaction_amount,int):
        total_amount += transaction_amount

  return total_amount

def add_transaction(amount:str, category:str, date:str, description:str):
  """Add expense to tracker"""
  categoryExists = transactions.get(category)

  if categoryExists is None:
    transactions.update({category:[{"date":date,"amount":int(amount),"description": description}]})
  else:
    categoryExists.append({
      "date": date,
      "amount": int(amount),
      "description": description
    })

  return True

def average_by_category():
  category_totals: list[dict[str,float]] = []

  for category in transactions:
    category_total = 0
    count = 0

    for transaction in transactions[category]:
      amount = transaction.get("amount")

      if isinstance(amount,int):
        category_total += amount
        count += 1

    category_totals.append({category: category_total/count})

  return category_totals

def monthly_total(date: str):
    total_amount = 0
    for category_name in transactions:
        for transaction in transactions[category_name]:
            transaction_date = transaction.get("date")
            transaction_amount = transaction.get("amount")

            if isinstance(transaction_date, str) and isinstance(transaction_amount, int):
                transaction_month = datetime.strptime(
                    transaction_date, "%Y-%m-%d"
                ).strftime("%Y-%m")

                if date == transaction_month:
                    total_amount += transaction_amount
    return total_amount
