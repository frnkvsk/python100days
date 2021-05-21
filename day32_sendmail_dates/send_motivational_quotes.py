import random
import smtplib
import datetime as dt

MY_GOOGLE = "@gmail.com"
MY_YAHOO = "@yahoo.com"
SMTP_GMAIL = "smtp.gmail.com"
SMTP_YAHOO = "smtp.mail.yahoo.com"
MY_GOOGLE_PW = ""
MY_YAHOO_PW = ""

now = dt.datetime.now()
weekday = now.weekday() # today == 3
if weekday == 3:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP(SMTP_YAHOO, port=587) as connection:
        connection.starttls()
        connection.login(user=MY_YAHOO, password=MY_YAHOO_PW)
        connection.sendmail(
            from_addr=MY_YAHOO,
            to_addrs=MY_GOOGLE,
            msg=f"Subject:Thursday Motivation\n\n{quote}"
        )