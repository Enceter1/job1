def draw_rectangle(width, height):
    print ("|" + "-" * (width - 2) + "|")
    for i in range(2, height):
        print("|" + " " * (width-2) + "|")
    print ("|" + "-" * (width - 2) + "|")

draw_rectangle(10, 7)