# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now= datetime.datetime.now()
name_list=[]
def date_check():
    data = pandas.read_csv("/Users/tharm/PycharmProjects/PythonProject/birthday-wisher-extrahard-start/birthdays.csv")
    for x in data.name:
        name_list.append(x)
    for actual_name in name_list:
        row= data[data.name==actual_name]
        if row.month.values[0]==now.month and row.day.values[0]==now.day:
            with open(f"letter_templates/{chosen_letter}") as letter:
                letter_content = letter.read()
                letter_content = letter_content.replace("[NAME]", f"{actual_name}")
                connection.sendmail(from_addr=email, to_addrs=email,
                                    msg=f"Subject: HAPPY BIRTHDAY!\n\n {letter_content}")
                print("email sent!")

letter_list= ["letter_1.txt", "letter_2.txt","letter_3.txt"]
chosen_letter= random.choice(letter_list)
# # #setup email connection
connection= smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=email, password=password)


date_check()

                
