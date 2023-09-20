def Leapyear(n):
  if (n % 4 == 0 and n% 100 != 0) or n%400==0:
    return True
  else:
    return False

n=int(input("Enter year:"))
if Leapyear(n):
  print(f"It is leap year")
else:
  print(f"It is not leap year")
    