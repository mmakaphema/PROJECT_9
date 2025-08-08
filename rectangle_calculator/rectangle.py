#CALCULATING THE AREA AND PERIMETER OF A RECTANGLE
import calculations

length = float(input("Enter the length of the rectangle:"))
width = float(input("Enter the width of the rectangle:"))

area = calculations.area(length, width)
perimeter = calculations.perimeter(length, width)

print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")
