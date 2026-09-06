from utils import (
  add_transaction,
  average_by_category,
  monthly_total,
  print_category,
  total_expenses,
  transactions,
  validate_date,
)


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
      if validate_date(date) is False:
        return "Date is invalid"

      description = user_ip[4]
      if description.isdigit():
        return "Description should be string"

      if add_transaction(amount,category,date,description) is True:
        print("Success")

    case "view_category":

      if len(user_ip) < 2:
        return "Provide proper format view_category <category>"

      category = user_ip[1]
      if category.isdigit():
        return "Category should be string"

      categoryExists = transactions.get(category)

      if categoryExists is None:
        return "Category dosen't exists"

      print_category(category,categoryExists)

      return categoryExists

    case "total":
      print("Total Expenses: ", total_expenses())

    case "average_by_category":
      print("\n Average Expense by Category:")

      category_avg = average_by_category()

      for item in category_avg:
        for key, value in item.items():
          print(key, ": ",value)

    case "monthly_total":
      if len(user_ip) < 2:
        return "Provide proper format monthly_total YYYY-MM"

      date = user_ip[1]

      print("\n Monthly Total: ", date)
      print("\n Total Expense: $", monthly_total(date) )

    case "exit":
      return False
    case _:
      print("Invalid command")
