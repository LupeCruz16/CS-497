'''
4/3

initialize circle_points, square_points and interval to 0

Loop:

Generate random point x
Generate random point y
Calculate d = x * x + y * y

If d <= 1, increment circle_points.
Increment square_points 

Calculate:
pi = 4 * (circle_points / square_points)
'''

import random

# Initialize circle_points, square_points, and interval to 0
circle_points = 0
square_points = 0
interval = 1000

# Loop
for _ in range(interval):
    # Generate random point x and y
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    # Calculate d = x * x + y * y
    d = x * x + y * y
    
    # If d <= 1, increment circle_points
    if d <= 1:
        circle_points += 1
    
    # Increment square_points
    square_points += 1

# Calculate pi
pi = 4 * (circle_points / square_points)

print("Approximation of pi:", pi)
