import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

if __name__ == '__main__':

    # Sample data points
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([5, 3, 8, 2, 7, 4, 6, 3, 9, 1])

    # Coordinates of the new point to interpolate
    x_new = 3.5
    y_new = 6.5

    # Calculate Delaunay triangulation
    points = np.array(list(zip(x, y)))
    tri = Delaunay(points)

    # Find the containing triangle for the new point
    triangle_index = tri.find_simplex((x_new, y_new))

    # If the point is outside the convex hull, it won't have a containing triangle
    if triangle_index == -1:
        print("The point is outside the convex hull of the data points.")
    else:
        # Get the indices of the three vertices of the containing triangle
        vertices = tri.simplices[triangle_index]

        # Coordinates of the vertices of the containing triangle
        x_triangle = x[vertices]
        y_triangle = y[vertices]

        # Calculate the barycentric coordinates of the new point within the triangle
        bary_coords = tri.transform[triangle_index, :3].dot(np.array([x_new, y_new]) - tri.transform[triangle_index, 2])

        # Interpolate the value at the new point using barycentric interpolation
        interpolated_value = np.sum(bary_coords * y_triangle)

        print("Interpolated value at ({}, {}): {:.2f}".format(x_new, y_new, interpolated_value))

        # Plot the scatter plot and the triangulation
        plt.scatter(x, y, color='blue', label='Data Points')
        plt.fill(x_triangle, y_triangle, color='red', alpha=0.5, label='Containing Triangle')
        plt.scatter(x_new, y_new, color='green', label='New Point')
        plt.legend()
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Delaunay Triangulation Interpolation')
        plt.grid()
        plt.show()
