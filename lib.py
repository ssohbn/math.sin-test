import math


# find value to go from
# previous to next
# change from to go from 3 to 6 would be 2.
# usable for stretching or shrinking a value
# to an expected range
def normalize(prev: int, new: int) -> float:
	return new/prev


def oscillation_point(hertz: float) -> int:
	hertz = math.degrees(math.pi * hertz)
	return 1