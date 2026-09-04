
def startUp():
  print("\n\t\t********** Personal Finance Tracker **********\t\n")
  print("Commands: \n")

  multiLine = """
   \tadd <amount> <category> <date> <description>
   \tview_category <category>
   \ttotal
   \taverage_by_category
   \tmonthly_total <YYYY-MM>
   \texit\n"""

  print(multiLine)

def main():
  startUp()
  while True:
    user_ip = input(">>> ").lower().split(" ")[0]

    match user_ip:
      case "add":
        print("Add")
      case "view_catagory":
        print("view_catagory")
      case "total":
        print("total")
      case "average_by_catagory":
        print("averag_by_catagory")
      case "monthly_total":
        print("monthly_total")
      case "exit":
        break
      case _:
        print("Invalid command")


if __name__ == "__main__":
  main()
