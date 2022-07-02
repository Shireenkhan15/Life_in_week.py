age_remaining=int(input("enter age"))
#  here we count the age till 90 thats why we are taking 90 - remaning age
year_remaining= 90-age_remaining
days_remaining=year_remaining*365
week_remaining=year_remaining*52
months_remaining=year_remaining*12
message = f"you have {days_remaining} days ,{week_remaining} weeks,and {months_remaining} months left."
print(message)