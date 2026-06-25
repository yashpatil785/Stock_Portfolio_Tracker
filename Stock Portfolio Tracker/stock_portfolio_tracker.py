print('\n -------Weclome our Stock Portfolio Tracker Project-------')   #tagline

stock_prices= {
    "TSLA":180,
    "AAPL":250,
    "GOOGL":150,
    "MSFT":400,                   #stocks companies list 
    "META":500,
    "NFLX":650,
    "NVIDA":1200,
    "ASIANPAINT":2800,
    "RELIANCE":1450,
    "TCS":3600,
    "INFY":1650,
    "SBIN":900
}

print(stock_prices)

Total_investment = 0    #total investment decleared by 0

n = int(input("How many stock you want: "))   #enter user the how many stock compaines list

for i in range(n):  
    stock_list = input("Enter the stock name: ").upper()   #enter user stock name by use upper function
    stock_Qty = int(input("Enter the stock Quantity: "))   #enter user how much stock quantity
    
    if stock_list in stock_prices:
        price = stock_prices[stock_list]                          #show price of stock compaines price also show stock compaines list
        investment = price * stock_Qty                            #investment formula of price * stock qty
        print(f"{stock_list}:{price}*{stock_Qty}={investment}")
        Total_investment += investment                            #total investment declare by investment
    else:
        print("Stock not found")                                #stock not found

print("\n-----Show Portfolio-----")
print("Total_investment", Total_investment)          #show total investment 
