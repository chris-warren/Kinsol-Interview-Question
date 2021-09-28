# Kinsol-Interview-Question

cartesian_coords_to_line.py

Author: Chris Warren
Interview Question

This program converts two points into a line in standard form

If this code was being used in a larger system, I probably would have created a line and point objects,
but that didnt seem necessary for this task

Pylint was used to ensure PEP-8 formatting
	- This was my first time using a PEP-8 plugin, it raised falgs for my single letter
		variable names, but I assumed that was fine

Pytest was used for testing

test cases:
	1) basic test with known int values/n
	2) basic test with known float values/n
	3) basic test with large known values/n
	4) checking that expressions are simplified/n
	5) generating values from -10 to 10 and checking that the function holds tru with input/n
	6) wrong number of inputs/n
	7) wrong datatypes/n
	8) two of the same points/n
	9) leftmost point is p2/n
	10) vertical line/n
	11) horizontal line/n
	12) test with point (0,0)/n
