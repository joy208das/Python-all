'''find how many days in a month'''

def in_year(year):
    if year%4==0:
        return True
    else:
        return False
 

def find(year,month):
    days_month=[31,28,31,30,31,30,31,31,30,31,30,31]
    if month ==2 and in_year(year):
       return 29
    else :
        return days_month[month-1]     




year=int(input("what is the year: "))
month=int(input("what is the month: "))
days=find(year,month)

print(f"there are {days} days in this month")

"""for multiple line use double inverted comma"""
#days_month={"31","28","31","30","31","30","31","31","30","31","30","31"}