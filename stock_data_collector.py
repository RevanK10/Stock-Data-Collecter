#Libraries imported
import yfinance as yf

#Variables used
user_choice = ''
stock = ''
time = ''
stock_choices = ['tesla', 's&p 500', 'apple', 'bitcoin', 'dogecoin', 'ethereum']

#Welcome message
print("Welcome!")
print("Here you can view historical data of stocks.")

#While loop that allows the statements to be repeated until the user quits the program
while user_choice != 2:
  stock = ''
  time = ''
  
  #Options available
  print("Options:")
  print("1: Check historical data")
  print("2: Quit")

  #Validating the user's input based on the options
  while True:
    user_choice = input()
    try:
      user_choice = int(user_choice)
      break
    except ValueError:
      print("Enter an integer of either 1 or 2")

    while user_choice != 1 or user_choice != 2:
      if user_choice == 1 or user_choice == 2:
        break
      else:
        print("Enter a vlaue of 1 or 2")
  
  #Asking the user for input about their chosen stock and validating the input
  if user_choice == 1:
    while stock not in stock_choices:
      print("Would you like to check the data of Tesla, S&p 500, Apple, Bitcoin, Dogecoin, or Ethereum")
      stock = input()
      stock = stock.lower()
      if stock in stock_choices:
        break
      else:
        print("Enter one of the given choices")

    #Taking input for time period of data required and validation for the input
    print("Enter how many days worth of data you wish to see? If you want to see all days, enter 'max' or enter the number of days.")
    while time != 'max' or int(time) % 1 != 0:
      time = input()
      if time == 'max':
        break
      elif int(time) % 1 == 0:
        time = time + 'd'
        break
      else:
        print("Enter max for all days of data, or enter the nymber of days!")
    
    #Performing web scraping based on the stock and time period chosen
    if stock == 'tesla':
      info = yf.Ticker("TSLA")
      data = info.history(period=time)
      print(data)
    elif stock == 's&p 500':
      info = yf.Ticker("^GSPC")
      data = info.history(period=time)
      print(data)
    elif stock == 'apple':
      info = yf.Ticker("AAPL")
      data = info.history(period=time)
      print(data)
    elif stock == 'bitcoin':
      info = yf.Ticker("BTC-USD")
      data = info.history(period=time)
      print(data)
    elif stock == 'dogecoin':
      info = yf.Ticker("DOGE-USD")
      data = info.history(period=time)
      print(data)
    else:
      info = yf.Ticker("ETH-USD")
      data = info.history(period=time)
      print(data)
      
  #Qutting the program if the user chooses option two
  if user_choice == 2:
    print("Hope you come again.")
    break
