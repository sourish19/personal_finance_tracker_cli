from utils import validateDate

transactions:dict[str,list[dict[str,str|int]]] = {}

def parse_input(user_ip: list[str]):
  """Parse user command and return components"""

  match user_ip[0]:
    case "add":

      if len(user_ip) < 5:
        return "Provide proper format add <amount> <category> <date> <description>"

      amount = user_ip[1]
      if amount.isdigit() is False:
        return "Amount should be positive integer"

      category = user_ip[2]
      if category.isdigit():
        return "Category should be string"

      date = user_ip[3]
      if validateDate(date) is False:
        return "Date is invalid"

      description = user_ip[4]
      if description.isdigit():
        return "Description should be string"

      categoryExists = transactions.get(category)

      if categoryExists is None:
        transactions.update({category:[{"date":date,"amount":amount}]})
      else:
        categoryExists.append({
          "date": date,
          "amount": amount
        })

      return "Success"

    case "view_category":

      if len(user_ip) < 2:
        return "Provide proper format view_category <category>"

      category = user_ip[1]
      if category.isdigit():
        return "Category should be string"

      categoryExists = transactions.get(category)

      if categoryExists is None:
        return "Category dosen't exists"

      print(categoryExists)

      return categoryExists

    case "total":
      print("total")
    case "average_by_category":
      print("averag_by_category")
    case "monthly_total":
      print("monthly_total")
    case "exit":
      return False
    case _:
      print("Invalid command")


def add_transaction(amount, category, date, description):
    """Add expense to tracker"""
    pass

def get_total_by_category():
    """Return dict with category totals"""
    pass
