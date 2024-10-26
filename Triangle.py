"""
This module contains a function to classify triangles based on side lengths.
"""

def classify_triangle(side_a, side_b, side_c):
    """
    Classify a triangle based on the lengths of its sides.
    
    Parameters:
        side_a, side_b, side_c: lengths of the triangle sides
        
    Returns:
        A string describing the type of the triangle.
    """
    # Check for valid input
    if side_a > 200 or side_b > 200 or side_c > 200:
        return 'InvalidInput'
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return 'InvalidInput'
    if not (isinstance(side_a, int) and isinstance(side_b, int) and isinstance(side_c, int)):
        return 'InvalidInput'
    # Check for triangle inequality
    if side_a >= (side_b + side_c) or side_b >= (side_a + side_c) or side_c >= (side_a + side_b):
        return 'NotATriangle'
    # Classify the triangle
    if side_a == side_b == side_c:
        return 'Equilateral'
    sides_squared = sorted([side_a ** 2, side_b ** 2, side_c ** 2])
    if sides_squared[0] + sides_squared[1] == sides_squared[2]:
        return 'Right'    
    if side_a != side_b and side_b != side_c and side_a != side_c:
        return 'Scalene'    
    return 'Isosceles'
