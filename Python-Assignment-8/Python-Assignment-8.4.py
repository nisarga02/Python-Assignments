def convert_negative_coordinates(coordinates):
    # Find the minimum x-coordinate and y-coordinate values
    min_x = min(coord[0] for coord in coordinates)
    min_y = min(coord[1] for coord in coordinates)

    # Calculate the offset values
    offset_x = abs(min_x)
    offset_y = abs(min_y)

    # Add the offset values to all coordinates
    converted_coordinates = [(coord[0] + offset_x, coord[1] + offset_y) for coord in coordinates]

    return converted_coordinates

# Test the function with the given input
input_coordinates = [(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
output_coordinates = convert_negative_coordinates(input_coordinates)
print(output_coordinates)
