a = {1: "one", 2: "three"}
a1 = {2: "two"}

# updates the value of key 2
a.update(a1)

print(a)

a1 = {3: "three"}

# adds element with key 3
a.update(a1)

print(a)
