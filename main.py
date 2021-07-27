pi = 22/7
print("Area and Perimeter Calculator")
print("-----------------------------")
print("1=Area | 2=Perimeter")
option = int(input("Enter your choice: "))
if option == 1:
	print("Shapes: 1=Square | 2=Rectangle | 3=Circle | 4=Triangle | 5=Trapezium")
	o2 = int(input("Enter shape: "))
	if o2 == 1:
		side = int(input("Enter side: "))
		print("Area of square is: ", side * side)
	elif o2 == 2:
		length = int(input("Enter length: "))
		breadth = int(input("Enter breadth: "))
		print("Area of rectangle is: ", length * breadth)
	elif o2 == 3:
		radius = int(input("Enter radius: "))
		print("Area of circle is: ", pi * radius * radius)
	elif o2 == 4:
		base = int(input("Enter base: "))
		height = int(input("Enter height: "))
		print("Area of triangle is: ", 1/2 * base * height)
	elif o2 == 5:
		s = int(input("Enter one side: "))
		s2 = int(input("Enter another side: "))
		h = int(input("Enter height: "))
		print("Area of trapezium is: ", h * (s + s2) / 2)
	else:
		print("Invalid input")
elif option == 2:
	print("Shapes: 1=Sqaure | 2=Rectangle | 3=Circle | 4=Triangle")
	o3 = int(input("Enter choice: "))
	if o3 == 1:
		side2 = int(input("Enter side: "))
		print("Perimeter of square is: ", side2 + side2 + side2 + side2)
	elif o3 == 2:
		l = int(input("Enter length: "))
		b = int(input("Enter breadth: "))
		print("Perimeter of rectangle is: ", 2 * (l + b))
	elif o3 == 3:
		r = int(input("Enter radius: "))
		print("Circumference of circle is: ", 2 * pi * r)
	elif o3 == 4:
		i = int(input("Enter 1st side: "))
		i2 = int(input("Enter 2nd side: "))
		i3 = int(input("Enter 3rd side: "))
		print("Perimeter of triangle is: ", i + i2 + i3)
	else:
		print("Invalid input")
else:
	print("INVALID")
