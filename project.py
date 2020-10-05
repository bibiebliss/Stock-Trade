"""CSC 161 Project III

Blessing Babajide
Lab Section TR 12:30 - 1:45pm
Fall 2019
"""

import datetime
import calendar
from tradinglib import Stock   # extra credit file made and imported


list_Date, list_Open, list_High, list_Low = [], [], [], []
list_Close, list_Adj_Close, list_Volume = [], [], []


def extract(file):
    filedata = open(file, "r")
    lines = filedata.readlines()
    for line in lines[1:]:
        Date, Open, High, Low, Close, Adj_Close, Volume = line.split(",")
        list_Date.append(Date)
        list_Open.append(Open)
        list_High.append(High)
        list_Low.append(Low)
        list_Close.append(Close)
        list_Adj_Close.append(Adj_Close)
        list_Volume.append(Volume)


def test_data(filename, col, day):
    """A test function to query the data you loaded into your program.

    Args:
        filename: A string for the filename containing the stock data,
                  in CSV format.

        col: A string of either "date", "open", "high", "low", "close",
             "volume", or "adj_close" for the column of stock market data to
             look into.

             The string arguments MUST be LOWERCASE!

        day: An integer reflecting the absolute number of the day in the
             data to look up, e.g. day 1, 15, or 1200 is row 1, 15, or 1200
             in the file.

    Returns:
        A value selected for the stock on some particular day, in some
        column col. The returned value *must* be of the appropriate type,
        such as float, int or str.
    """
    extract(filename)
    col = col.lower()
    if col == "date":
        value = (list_Date[day-1])
        print(value)
    elif col == "open":
        value = (float(list_Open[day-1]))
        print(value)
    elif col == "high":
        value = (float(list_High[day-1]))
        print(value)
    elif col == "low":
        value = (float(list_Low[day-1]))
        print(value)
    elif col == "close":
        value = (float(list_Close[day-1]))
        print(value)
    elif col == "adj close":
        value = (float(list_Adj_Close[day-1]))
        print(value)
    elif col == "volume":
        value = (list_Volume[day-1])
        print(value)
    return value


def alg_moving_average(filename):
    """This function implements the moving average stock trading algorithm.

    The CSV stock data should be loaded into your program; use that data to
    make decisions using the moving average algorithm.

    Any bookkeeping setup from Milestone I should be called/used here.

    Algorithm:
    - Trading must start on day 21, taking the average of the previous 20 days.
    - You must buy shares if the current day price is 5%, or more, lower than the moving average.
    - You must sell shares if the current day price is 5% higher, or more than the moving average.
    - You must buy, or sell 10 stocks per transaction.
    - You are free to choose which column of stock data to use (open, close, low, high, etc)

    Args:
        A filename, as a string.

    Returns:
        Two values, stocks and balance OF THE APPROPRIATE DATA TYPE.

    Prints:
        Nothing.
    """
    # Last thing to do, return two values: one for the number of stocks you end up
    # owning after the simulation, and the amount of money you have after the simulation.
    # Remember, all your stocks should be sold at the end!
    extract(filename)
    stocks_owned = 0
    cash_balance = 1000
    _sum = 0
    day = 0
    for i in list_Open:
        i = float(i)
        _sum += i  # increment the values
        day += 1   # increment the no of days
        while day > 19:       #gets here when day = 20 sum
            avg = _sum/20
            if i <= (0.95 * avg):
                cash_balance, stocks_owned = Stock(stocks_owned, cash_balance, i, 10).buy_stock()
            elif i >= (1.05 * avg):
                cash_balance, stocks_owned = Stock(stocks_owned, cash_balance, i, 10).sell_stock()
            day = 0   # revert day count to 0 to start all over
            _sum = 0  # revert sum to 0 to start new set
    cash_balance, stocks_owned = Stock(stocks_owned, cash_balance, i, stocks_owned).sell_stock()

    return stocks_owned, cash_balance


def alg_mine(filename):
    """This function implements the student's custom trading algorithm.

    Using the CSV stock data that should be loaded into your program, use
    that data to make decisions using your own custome trading algorithm.

    Also, any bookkeeping setup in Milestone I should be called/used here.

    Args:
        A filename, as a string.

    Algorithm:
    - uses the list_open column of stock data
    - buy or sell 10 stocks per transaction
    - buy stocks if the given day is a monday or if it is another weekday in December or January
    - sell stocks if the given day is a friday or if it is another weekday in November, March or April

    Returns:
        Two values, stocks and balance OF THE APPROPRIATE DATA TYPE.

    Prints:
        Nothing.
    """
    extract(filename)
    cash_balance = 1000
    stocks_owned = 0
    dict_wd = dict()
    dict_m = dict()
    for date in list_Date:      # get the weekday for each date in list
        year, month, day = date.split("-")
        year, month, day = int(year), int(month), int(day)
        data = datetime.date(year, month, day).weekday()
        weekday = calendar.day_name[data]
        for i in list_Open:
            dict_wd[weekday] = float(i)
            for key, val in dict_wd.items():
                if key == "Monday": 
                    cash_balance, stocks_owned = Stock(stocks_owned, cash_balance, val, 10).buy_stock()
                elif key == "Friday":
                    cash_balance, stocks_owned = Stock(stocks_owned, cash_balance, val, 10).sell_stock()
                else:
                    dict_m[month] = float(i)
                    for key, value in dict_m.items():
                        if key == 12 or key == 1:
                            cash_balance, stocks_owned = Stock(stocks_owned, cash_balance, value, 10).buy_stock()
                        elif (key == 11 or
                              key == 4):
                            cash_balance, stocks_owned = Stock(stocks_owned, cash_balance, value, 10).sell_stock()                  
        cash_balance, stocks_owned = Stock(stocks_owned, cash_balance, float(i), stocks_owned).sell_stock()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        return stocks_owned, cash_balance

    # Last thing to do, return two values: one for the number of stocks you end up
    # owning after the simulation, and the amount of money you have after
    # the simulation.
    # Remember, all your stocks should be sold at the end!
    return stocks_owned, cash_balance

def main():
    # My testing will use AAPL.csv or MSFT.csv
    filename = input("Enter a filename for stock data (CSV format): ")

    # Call your moving average algorithm, with the filename to open.
    alg1_stocks, alg1_balance = alg_moving_average(filename)

    # Print results of the moving average algorithm, returned above:
    print("The results of the moving algorithm are stocks = {0} and balance = ${1:0.4f}".format(alg1_stocks, alg1_balance))

    # Now, call your custom algorithm!
    alg2_stocks, alg2_balance = alg_mine(filename)

    # Print results of your algorithm, returned above:
    print("The results of my algorithm are stocks = {0} and balance = ${1:0.4f}".format(alg2_stocks, alg2_balance))

if __name__ == '__main__':
    main()  
