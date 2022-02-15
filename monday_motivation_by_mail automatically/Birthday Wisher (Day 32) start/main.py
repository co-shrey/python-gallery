import smtplib

import random
my_m="musicalsvirtuoso@gmail.com"
passw="shreya@33"
# connection=smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_m,password=passw)
# connection.sendmail(from_addr=my_m,to_addrs="emusic553@gmail.com",msg="hello")


import datetime as dt
now=dt.datetime.now()

day_w=now.weekday()
if day_w==5:
    with open("quotes.txt") as quote_f:
        all_q=quote_f.readlines()
        quote=random.choice(all_q)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_m,password=passw)
        connection.sendmail(from_addr=my_m,to_addrs="emusic553@gmail.com",msg=f"Monday_motivation\n\n{quote}")








