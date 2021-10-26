f = open("test_file.csv", "a")
f.write('5,70,150,461,10.5\n6,40,4456,356,67.55')
f.close()

f = open("test_file.csv", "r")
print(f.read())
f.close()
