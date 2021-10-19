# Adding a placeholder to display the price

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# Price to be displayed with decimal values

price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Adding multiple placeholder to display the price

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
