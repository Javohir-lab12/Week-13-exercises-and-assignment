import datetime as dt
exam_year = int(input("Enter exam year: "))
exam_month = int(input("Enter exam month: "))
exam_day = int(input("Enter exam day: "))
exam_date = dt.date(year=exam_year, month=exam_month, day=exam_day)
today = dt.date.today()
difference = exam_date - today
days = difference.days
if days == 0:
    print("Good luck! The exam is today.")
elif days < 0:
    print(f"The exam was {days} days ago.")
else:
    print(f"You have {days} days left to study!")