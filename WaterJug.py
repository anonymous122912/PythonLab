def pour_water(jugA, jugB):
	# max1, max2, fill = 3, 4, 2
	# max1, max2, fill = 5, 12, 1
	print("%d \t %d" % (jugA, jugB))
	if jugB == fill:
		return
	elif (jugB == max2) or (jugA != 0 and jugB == 0):
		pour_water(0, jugA)
	elif jugA == fill:
		pour_water(jugA, 0)
	elif jugA < max1:
		pour_water(max1, jugB)
	elif jugA < (max2-jugB):
		pour_water(0, (jugA+jugB))
	else:
		pour_water(jugA-(max2-jugB), (max2-jugB)+jugB)


max1 = int(input("Enter max capacity of Jug A : "))
max2 = int(input("Enter max capacity of Jug B : "))
fill = int(input("Enter the quantity to be filled in Jug B : "))
print("Jug A  Jug B")
pour_water(0, 0)










