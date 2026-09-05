from datetime import datetime

transactions:dict[str,list[dict[str,str|int]]] = {}

def validateDate(date: str):
  try:
    if date != datetime.strptime(date,"%Y-%m-%d").strftime("%Y-%m-%d"):
      raise ValueError
    return True
  except ValueError:
    return False

def printCategory(category:str, categoryExists:list[dict[str, str | int]]):
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

def totalExpense():
  total_amount = 0
  category_transactions = transactions.values()

  for transaction_list in category_transactions:
    for transaction in transaction_list:
      transaction_amount = transaction.get("amount")
      if isinstance(transaction_amount,int):
        total_amount += transaction_amount

  return total_amount
