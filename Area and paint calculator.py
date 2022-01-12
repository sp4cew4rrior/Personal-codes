#That program will calculate the area of a wall and how much paint you will need to paint it completely.(Knowing that one can of pait paints 2m² of the wall).
#The lines 3 to 5 asks which are the height and the width of the wall.
h = float(input('Please insert the height of the wall in meters: '))
w = float(input('Now, please insert the width in meters: '))
a = h * w
#Now that will calculate how many cans of paint will be needed.
p = a / 2
print('The are of the wall is {}, and will be needed {} can of paint to fully paint the wall.'.format(a, p))



