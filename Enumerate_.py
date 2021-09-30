
colors = ['Violet', 'Gray', 'Pink', 'Blue']

for item in colors:
    print(item)

for index, colors in enumerate(colors):
    print(index, colors)

for index, colors in enumerate(colors, start=1):
    print(index, colors)
