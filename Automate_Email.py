from email.message import EmailMessage
import ssl
import smtplib

#Email addresses
email_sender = 'letzspam1@gmail.com'
email_password = "qjps bqyc owpa olzp"
email_receiver = "devenbariya@gmail.com"

#Setting up the mail body.....
subject = "Testing the automation."
stock_name = "MRF"
Current_Price = 100000
Buying_Price = 80000
profit = Current_Price - Buying_Price
loss = Buying_Price - Current_Price
quantity = 100
body = f"""
This is an email notifying about your stock prices as a daily routine.
Stock Name:- {stock_name} , Current Price:- ₹{Current_Price}
Quantity:- {quantity}, \nProfit compared to when bought:- ₹{profit}
"""

em = EmailMessage()
em['From'] = email_sender 
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())