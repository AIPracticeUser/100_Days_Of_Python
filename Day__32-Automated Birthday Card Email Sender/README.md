## Day 32- Automated Birthday Card Email
AIM: Email SMTP and datetime module

File : mywork.py


# Important notes
## SMTP
- SMTP = Simple Transfer Protocol
- An application that is used by mail servers to send, receive and relay outgoing email between senders and receivers
- ![img.png](img.png)
- import smtplib #Importing SMTP library
- connection = smtplib.SMTP("smtp.gmail.com") #creating an object using smtplib with parameter as spectific server(such as smtp.gmail.com)
- ![img_1.png](img_1.png)
- connection.starttls #tls is transport layer security, for making connection secure
- connection.login(user="my_email", password="password") #login to email server
- connection.sendmail(from_addr="my_email", to_addrs="recipient_email, msg='Hello") 

## Datetime
- import datetime as dt     #importing datetime module
- now = dt.datetime.now()   #now() method includes the all the time including the year, month, day, time etc
- year = now.year           #can specify select the year attribute from the now
- print(type(now))          #returns as a datetime object
- print(type(year))          #returns an integer type, hence able to do condition check on it 
- day_of_week = now.weekday() #specify week day attribute
- print(day_of_week)        #returns an integer. If "1" means tuesday, since counting start from 0
- date_of_birth = dt.datetime(year=1995,month=12,day=25) #year, month, day is the only requirement for datetime object. This returns "1995-12-15 00:00:00" with 00hrs,mins,secs as default value
- 


## Steps for Special Password for SMTP GMAIL PYTHON APPLICATION
1) Go to manage Google account

![img_2.png](img_2.png)
2) Go to security

![img_3.png](img_3.png)
3) Turn on 2-step Verification

![img_5.png](img_5.png)
4) After verification with OTP, app passwords section should appear

![img_6.png](img_6.png)
5) Create other(custom name), name it "birthday_wisher", then click on Generate

![img_7.png](img_7.png)

6) Copy the app password into the codes

![img_8.png](img_8.png)

## Automated Birthday Card Email project
file: mywork.py
### Note
Purely using to_dict() method will only return the column name
results:
{'name': {0: 'Test', 1: 'test2'}, 'email': {0: 'test@email.com', 1: 'test2@email.com'}, 'year': {0: 1961, 1: 1942}, 'month': {0: 12, 1: 3}, 'day': {0: 21, 1: 3}}

Hence need to use df.to_dict(orient="records")
[{'name': 'Test', 'email': 'test@email.com', 'year': 1961, 'month': 12, 'day': 21}, {'name': 'test2', 'email': 'test2@email.com', 'year': 1942, 'month': 3, 'day': 3}]

Example of email received

![image](https://user-images.githubusercontent.com/100339175/222682392-bed08842-c3db-4c94-a6e6-e8ede599b11d.png)
![image](https://user-images.githubusercontent.com/100339175/222682801-509be8a5-21da-4b00-8723-cca8cdef35f1.png)



