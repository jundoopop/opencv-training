def bilinear_interpolation(x, y, points):
    '''Interpolate (x,y) from values associated with four points.
    The four points are a list of four triplets: (x, y, value).
    The four points can be in any order. They should form a rectangle.
    '''
    # Sort the points by x, then by y
    points = sorted(points)
    # Get the values in the four corners
    (x1, y1, q11), (_x1, y2, q12), (x2, _y1, q21), (_x2, _y2, q22) = points

    # Compute the x and y distances from the lower left corner
    x2_x = x2 - x
    y2_y = y2 - y
    x_x1 = x - x1
    y_y1 = y - y1

    # Compute the weights for each corner based on the distance from that corner
    w1 = x2_x * y2_y
    w2 = x2_x * y_y1
    w3 = x_x1 * y2_y
    w4 = x_x1 * y_y1

    # Interpolate between the top two corners and the bottom two corners
    return (q11 * w1 + q21 * w2 + q12 * w3 + q22 * w4) / (w1 + w2 + w3 + w4)


# Define the known points
points = [(0, 0, 0), (0, 1, 1), (1, 0, 2), (1, 1, 3)]

# Define the x and y coordinates of the unknown point
x_new = 0.5
y_new = 0.5

# Perform bilinear interpolation
result = bilinear_interpolation(x_new, y_new, points)

print(result)
