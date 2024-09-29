# checks whether a point is within a quadrilateral space

def quad_checker(coord1, coord2, coord3, coord4, coord5): # kinda cheeks 
    sum_of_areas = 0
    quad_area = (coord2[0] - coord1[0]) * (coord3[1] - coord2[1])
    coords = [coord1, coord2, coord3, coord4, coord5]
    for i in range(4):
        if (i+1) < 4:
            area = 0.5 * (coords[i][0] * (coords[i+1][1]-coords[4][1]) + coords[i+1][0] * (coords[4][1] - coords[i][1]) + coords[4] * (coords[i][1] - coords[i+1][1]))
        else:
            area = 0.5 * (coords[i][0] * (coords[i-i][1]-coords[4][1]) + coords[i-i][0] * (coords[4][1] - coords[i][1]) + coords[4] * (coords[i][1] - coords[i-i][1]))
        sum_of_areas += area
    
    # ending code
    if sum_of_areas == quad_area:
        return True
    return False