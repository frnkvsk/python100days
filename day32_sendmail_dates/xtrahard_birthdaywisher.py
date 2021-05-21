##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import random
import smtplib
import datetime as dt
import pandas

MY_GOOGLE = "@gmail.com"
MY_YAHOO = "@yahoo.com"
SMTP_GMAIL = "smtp.gmail.com"
SMTP_YAHOO = "smtp.mail.yahoo.com"
MY_GOOGLE_PW = ""
MY_YAHOO_PW = ""


now = dt.datetime.now()

data = pandas.read_csv("birthdays.csv")
all_birthdays = data.to_dict(orient="records")
for birthday in all_birthdays:
    if birthday["month"] == now.month and birthday["day"] == now.day:
        random_int = random.randint(1, 3)
        filename = f"letter_{random_int}.txt"
        with open(filename) as file:
            letter = file.read()
            letter = letter.replace("[NAME]", birthday["name"])

        with smtplib.SMTP(SMTP_YAHOO, port=587) as connection:
            connection.starttls()
            connection.login(user=MY_YAHOO, password=MY_YAHOO_PW)
            connection.sendmail(
                from_addr=MY_YAHOO,
                to_addrs=birthday["email"],
                msg=f"Subject:Happy Birthday!\n\n{letter}"
            )