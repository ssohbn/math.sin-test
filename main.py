import math
import turtle
import lib

# screen size stuff
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 32

turtla = turtle.Turtle()
turtla.penup()

# iterate thru each horizontal pixel
# thingy on screen
for x in range(0, SCREEN_WIDTH): 

	# amount of waves that will be drawn
	hertz = 20
	hertz_as_degrees = math.degrees(math.pi * hertz)
	# normalize is used to bring 128
	# the previous max value,
	# to 360, the amount of degrees
	# in a full rotation
	#
	# normalized value allows us 
	# to shrink sine wave to something
	# that will fit on the screen.
	# shitty comments i dont know wat im saying
	#
	# it make it so i show frequency on the thing.
	# it also always take same length idk
	normalized_x = x * lib.normalize(SCREEN_WIDTH, hertz_as_degrees)
	# switch to radians because math.sin take radian value
	rads_x = math.radians(normalized_x)
	# sin returns a value from [-1, 1]
	# multiplying this value by half of the screen height
	# lets the value be stretched to fill
	# the whole screen
	y = int(math.sin(rads_x) * (SCREEN_HEIGHT/2))

	# translate x left 100 for visibility or whatever
	turtla.goto(x-100,y)
	print(f"{x}, {y}")
	turtla.pendown()
