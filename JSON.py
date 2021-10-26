
import json
# Code to convert JSON to Python
# In JSON:
x = '{ "name":"Jack", "age":45, "city":"New York"}'

# parse x:
y = json.loads(x)

# Results Python dictionary:
print(y["age"])

# Conversion of Python to  JSON
# a Python object (dict):
x = {
  "name": "Fabio",
  "age": 32,
  "city": "Paris"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
