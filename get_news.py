import requests
import datetime


class News:
    api_key = "1ef870c085d94b09a63d3acbfbcf416c"  # unique key
    head_url = "https://newsapi.org/v2/everything?"
    today = datetime.datetime.now().strftime("%dd %mm %YYYY")  # I took date range 1 day
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%dd %mm %YYYY")

    def __init__(self, interest, from_date=today, to_date=yesterday, language="en"):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        # Getting the url depends on different interests, date etc.
        url = f"{self.head_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"

        respond = requests.get(url)
        articles = respond.json()["articles"]
        body = ""
        for article in articles:
            body = body + article["title"] + "\n" + article["url"] + "\n\n"

        return body


if __name__ == "__main__":
    new = News("body building")
    print(new.get())
