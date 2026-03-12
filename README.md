# 📈 Stock Alert SMS App

A Python application that monitors stock price changes and sends SMS alerts when significant movements occur.

This project checks the stock price difference between the last two trading days. If the price change exceeds a defined threshold, it fetches related news articles and sends them as SMS alerts.

---

## 🚀 Features

* Fetch stock price data using an API
* Calculate percentage change in stock price
* Retrieve latest related news articles
* Send SMS notifications using Twilio
* Store API keys securely using environment variables

---

## 🛠️ Technologies Used

* Python
* Requests
* Twilio API
* News API
* Alpha Vantage API
* python-dotenv

---

## 📂 Project Structure

Stock-Alert-App
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/atul-23012006/Stock-Alert-App.git
cd Stock-Alert-App

---

### 2. Install dependencies

pip install -r requirements.txt

---

### 3. Create a `.env` file

Add the following variables in your `.env` file:

STOCK_API_KEY=your_alpha_vantage_api_key
NEWS_API_KEY=your_news_api_key
TWILIO_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_number
MY_PHONE_NUMBER=your_phone_number

---

### 4. Run the application

python main.py

---

## 📊 How It Works

1. Fetch stock price data from Alpha Vantage.
2. Calculate percentage change between yesterday and the previous trading day.
3. If the change exceeds the threshold (e.g., 5%), fetch related news articles.
4. Send the top news headlines via SMS using Twilio.

---

## 🔐 Security

Sensitive information such as API keys and credentials are stored in a `.env` file and excluded from Git using `.gitignore`.

---

## 📌 Future Improvements

* Support monitoring multiple stocks
* Email notifications
* Web dashboard for tracking stocks
* Automated scheduled checks

---

## 👨‍💻 Author

Atul Bharadwaj

GitHub: https://github.com/atul-23012006
