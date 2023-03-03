# import smtplib
#
# my_email = "stevecho008@gmail.com"
# password = "lwpszfnhexfdjhpr"
#
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="aprilneo007@hotmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email"
#                         )

# import datetime as dt
#
# now = dt.datetime.now()
# #year
# year = now.year
# print(year)
# print(type(year))
# #current time
# print(now)
# print(type(now))
# #condition check for year
# if year == 2023:
#     print("Don't need to wear face mask anymore")
# #day of the week. 0=Monday, 1=Tuesday etc
# day_of_week = now.weekday()
# print(day_of_week)
# #enter birthday through datetime
# date_of_birth = dt.datetime(year=1995, month=12, day=15)
# print(date_of_birth)
#-------------------------------------------------------------------------
import datetime as dt
import random
import smtplib
MY_EMAIL = "stevecho008@gmail.com"
MY_PASSWORD = "lwpszfnhexfdjhpr"
quote = ""

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 6:
    with open("quotes.txt", "r") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="aprilneo007@hotmail.com",
                            msg=f"Subject:Sunday Motivation\n\n{quote}"
                        )




