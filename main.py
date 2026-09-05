from tracker import parse_input


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
    user_ip = input(">>> ").lower().split(" ")

    command = parse_input(user_ip)

    if command is False:
      break


if __name__ == "__main__":
  main()
