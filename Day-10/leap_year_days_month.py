def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:   # 400 diyeo div hole then leap year
                # print("Leap year")
                return True
            else:
                # print("Not leap year")
                return False
        else:   # only 100 diye gele not leap year
            print("leap year")
    else:   # need to div by 400 also
        # print("not leap year")
        return False
def days_in_month(year,month):
    """Takes a year and returns it"""
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month > 12 and month < 1:
        return "Give valid month"
    if is_leap(year) and month == 2:
          return 29
    return month_days[month -1]

year = int(input("Year"))
month = int(input("Enter a month: "))

days = days_in_month(year,month)
print(days)

