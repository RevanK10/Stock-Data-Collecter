The goal of the Stock Data Collector project is to create a reliable framework for obtaining, classifying, and archiving stock market data from multiple sources.

Data Collection: The historical data of each stock is scraped from their respective webpages in Yahoo Finance using the yfinance library. The company and the time period is specified by the user from one of the options, and these choices are used to retrieve the data from the webpages.

Choice Validation: The choices are validated through the use of while loops and if condtions to check if the recieved choice is the correct type or equal to specific value.

User Interface: A while loop is used to ensure that the user can look at data of different companies until they decided to stop the program. Each value required is asked as input and data is printed through the use of these options. The time period  always starts from the current date and the output will be the time period required by the user.
