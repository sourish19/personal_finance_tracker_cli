from datetime import datetime

def validateDate(date: str):
  try:
    if date != datetime.strptime(date,"%Y-%m-%d").strftime("%Y-%m-%d"):
      raise ValueError
    return True
  except ValueError:
    return False
