print("Paramjeetsinh Jadeja")
print("24BEE138")
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
x3 = float(input("Enter x3: "))
y3 = float(input("Enter y3: "))
if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
    print("All three points lie on a straight line.")
else:
    print("The points do not lie on a straight line.")
