def triangle(n, stars= 1, spaces= 9):
    if stars > n:
        return
    print(" " * spaces + "*" * stars)
    triangle(n, stars + 2, spaces - 1)
    
if __name__ == "__main__":
    triangle(5)