import yagmail
import pandas as pd
from get_news import News
import datetime

email = yagmail.SMTP(user="12345@gmail.com", password="123456")
data = pd.read_excel("people.xlsx")
data = data.dropna()

while True:
    if datetime.datetime.now() == 08.00:  # Program sends news every morning at 8.00 AM
        for idx, row in data.iterrows():
            instance = News(row["interest"])
            instance.get()

            email.send(to=row["email"],
                       subject=f"Your {row['interest']} news for today!",
                       contents=f"Guten Morgen {row['name']},\n See what's going on about {row['interest']} \n\n"
                                f"{instance.get()} \n\n Mert Güneş")
