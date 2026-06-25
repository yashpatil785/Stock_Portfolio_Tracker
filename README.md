# Stock_Portfolio_Tracker
A Python-based Stock Portfolio Tracker that calculates investment value for Indian and US stocks using dictionaries, user input, loops, functions, and file handling.
# 📈 Stock Portfolio Tracker

## 📌 Project Overview

The Stock Portfolio Tracker is a Python console-based application developed as part of the **CodeAlpha Python Programming Internship**.

The application allows users to enter stock names and quantities, calculates the investment value using predefined stock prices for both Indian and US companies, displays the total portfolio value, and generates a portfolio report in a text file.

---

# 🚀 Features

* Multiple stock support
* Indian and US stock portfolio
* User-friendly console interface
* Investment calculation
* Total portfolio value calculation
* Invalid stock validation
* Portfolio report generation (.txt)
* Clean and modular Python code

---

# 🛠 Technologies Used

* Python 3
* Dictionary
* Loops
* Conditional Statements
* Functions
* File Handling

---

# 📂 Project Structure

```text
CodeAlpha_StockPortfolioTracker/
│
├── stock_portfolio.py
├── portfolio_report.txt
├── README.md
└── screenshots/
```

---

# 📊 Sample Stocks

## 🇮🇳 Indian Stocks

* RELIANCE
* TCS
* INFY
* ASIANPAINT
* SBIN

## 🇺🇸 US Stocks

* AAPL
* TSLA
* MSFT
* GOOGL

---

# 💡 Project Logic

```text
START

Create a dictionary of stock names, prices and currencies.

Set total_investment = 0.

Ask the user how many stocks they want to enter.

Repeat for each stock:

    Input stock name.

    Input quantity.

    Check whether the stock exists.

    If stock exists:

        Get stock price.

        Calculate investment.

        Add investment to total_investment.

        Display stock details.

    Else:

        Display "Stock Not Found".

Display total portfolio value.

Save portfolio report into a text file.

END
```

---

# 🔄 Flowchart

```text
                 START
                    │
                    ▼
      Create Stock Dictionary
                    │
                    ▼
      total_investment = 0
                    │
                    ▼
 Ask Number of Stocks to Enter
                    │
                    ▼
      Input Stock Name & Quantity
                    │
                    ▼
      Stock Exists in Dictionary?
             ┌──────┴──────┐
             │             │
            No            Yes
             │             │
             ▼             ▼
     Display Error   Get Stock Price
             │             │
             │             ▼
             │   Calculate Investment
             │             │
             │             ▼
             │   Add to Total Investment
             │             │
             └──────┬──────┘
                    ▼
        More Stocks to Enter?
             ┌──────┴──────┐
             │             │
            Yes           No
             │             │
             └─────
```
