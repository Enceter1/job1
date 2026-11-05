def tapis(n):
    chars = "#" * n
    print("+" + "-" * (n+1) + "+")
    for i in range(n+1):
        print("[" + (chars[:-i] if i > 0 else chars) + " " + chars[:i] + "]")
        
    print("+" + "-" * (n+1) + "+")

tapis(10)
