import requests
import os
from flask import Flask, render_template, request
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

ALPHA_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"

ALPHA_KEY = os.environ["ALPHA_API_KEY"]
NEWS_KEY = os.environ["NEWS_API_KEY"]


@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        STOCK = request.form["stock"]
        COMPANY_NAME = request.form["company"]

        # -------- STEP 1: GET STOCK DATA --------
        stock_params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": STOCK,
            "apikey": ALPHA_KEY
        }

        stock_response = requests.get(ALPHA_URL, params=stock_params)
        stock_data = stock_response.json()

        if "Time Series (Daily)" not in stock_data:
            return render_template(
                "index.html",
                result={"error": "Unable to fetch stock data. API limit may be reached."}
            )

        dates = list(stock_data["Time Series (Daily)"])

        d1 = float(stock_data["Time Series (Daily)"][dates[0]]["4. close"])
        d2 = float(stock_data["Time Series (Daily)"][dates[1]]["4. close"])

        change = d1 - d2
        percent_change = round(abs(change) * 100 / d2, 2)

        direction = "🔺" if change > 0 else "🔻"

        # -------- STEP 2: GET NEWS --------
        news_params = {
            "q": COMPANY_NAME,
            "language": "en",
            "apiKey": NEWS_KEY
        }

        news_response = requests.get(NEWS_URL, params=news_params)
        news_data = news_response.json()

        if "articles" not in news_data:
            return render_template(
                "index.html",
                result={"error": "Unable to fetch news. API limit may be reached."}
            )

        articles = news_data["articles"][:3]

        headlines = []

        for article in articles:
            headlines.append({
                "title": article["title"],
                "description": article["description"]
            })

        result = {
            "stock": STOCK,
            "percent": percent_change,
            "direction": direction,
            "news": headlines
        }

        # -------- STEP 3: SEND SMS --------
        client = Client(account_sid, auth_token)

        message_text = f"{STOCK}: {direction}{percent_change}%\n\n"

        for article in headlines:
            message_text += f"{article['title']}\n{article['description']}\n\n"

        client.messages.create(
            body=message_text,
            from_=os.environ["TWILIO_PHONE"],
            to=os.environ["MY_PHONE"]
        )

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)