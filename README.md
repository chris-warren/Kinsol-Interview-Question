# Kinsol-Interview-Question

cartesian_coords_to_line.py

Author: Chris Warren
Interview Question

This program converts two points into a line in standard form

If this code was being used in a larger system, I probably would have created a line and point objects,
but that didnt seem necessary for this task

Pylint was used to ensure PEP-8 formatting

	This was my first time using a PEP-8 plugin, it raised flags for my single letter
		variable names, but I assumed that was fine

Pytest was used for testing

test cases:


	1) basic test with known int values
	
	2) basic test with known float values
	
	3) basic test with large known values
	
	4) checking that expressions are simplified
	
	5) generating values from -10 to 10 and checking that the function holds tru with input
	
	6) wrong number of inputs
	
	7) wrong datatypes
	
	8) two of the same points
	
	9) leftmost point is p2
	
	10) vertical line
	
	11) horizontal line
	
	12) test with point (0,0)
	
