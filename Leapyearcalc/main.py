from leap_year import days_in_month
year= int(input("What is the year :"))
month= int(input("What is the month :"))
days= days_in_month(year, month)
print(days)