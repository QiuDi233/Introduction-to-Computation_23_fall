n=int(input())
b=float(27+23+n/3)
w=float(n/(1.2))
if b<w:
    print("Bike")
if b>w:
    print("Walk")
if b==w:
    print("All")