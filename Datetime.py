# Importing datetime module and to display current date
import datetime

x = datetime.datetime.now()
print(x)

# To get return value of year and name of weekday

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
