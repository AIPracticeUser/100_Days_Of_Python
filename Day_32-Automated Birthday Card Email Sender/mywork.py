##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt
import pandas as pd
import random
import smtplib

MY_EMAIL = "mymail@gmail.com"
MY_PASSWORD = "my_password"

'''
Parameters:
now : datetime
    current date and time upon execution
current_month : integer
    current month
current_day : integer
    current day
record_found : integer
    index in the list if record found
birthday_found: boolean
    boolean true if month and day matches today's month and day, else false
'''

now = dt.datetime.now() #importing datetime module
current_month = now.month #find current month
current_day = now.day #find current day
birthday_found = False
record_found = 0

'''
Reading from birthdays.csv, converting to Dataframe and then to to_dict(orient="records")
'''
df = pd.read_csv('birthdays.csv') #using panda module to read birthday.csv
#example = df.to_dict()  #Purely to_dict will only return the column name as in the example
#print(example)
records_dict = df.to_dict(orient="records") #Hence by using (orient="records), we put the records into a list
#print(records_dict)

'''
Check in the records_dict, if current month and current day = dict's month and day
return: birthday_found = True if records found
'''
for i in range(0,len(records_dict)):
    if current_month == records_dict[i]["month"] and current_day == records_dict[i]["day"]:
        record_found = i
        birthday_found = True
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
'''
if birthday_found, select a random number from 1 to 3 and select the letter based on the chosen number
parameters:

random_num : integer
    random number from 1 to 3 based on random module
letter_selected : string
    f function string combination with random_num value
'''
if birthday_found:
    random_num = random.randint(1,3)
    letter_selected = f"letter_{random_num}.txt"

#using open method in directory letter_templates with 'r' as read mode, replace [NAME] with the name in the record
    with open(f"letter_templates/{letter_selected}", 'r') as letter:
        send_letter = letter.read()
        send_letter = send_letter.replace('[NAME]', records_dict[record_found]["name"])

# 4. Send the letter generated in step 3 to that person's email address.
    #sending email with smtp library
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=records_dict[record_found]["email"],
                            msg=f"Subject:Happy Birthday!\n\n{send_letter}" )



