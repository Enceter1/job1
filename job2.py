def draw_triangle(heigth):
    for i in range(heigth):
        print(" " * (heigth - 1 - i) + "/" + ("_" if i == heigth-1 else " ") * i*2 + "\\")




draw_triangle(5)