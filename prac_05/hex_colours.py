COLOUR_DICT = {"azure1": "#f0ffff", "cadetblue": "#5f9ea0v", "coral": "#ff7f50", "darkviolet": "#9400d3",
               "dimgray": "#696969", "gold1": "#ffd700", "medium": "#66cdaa", "oldlace": "#fdf5e6", "pink": "#ffc0cb"}
print(COLOUR_DICT)


colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    if colour_name in COLOUR_DICT:
        print(colour_name, "is", COLOUR_DICT[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()
