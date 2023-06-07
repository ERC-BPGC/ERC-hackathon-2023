import matplotlib.pyplot as plt
from shapely.geometry import LineString, Point, Polygon


# Walls represented as rectangles when viewed from top. The wall_array consists of an array of objects of the type Wall
class Wall:
    def __init__(self, centerX, centerY, length, width):
        self.centerX = centerX
        self.centerY = centerY
        self.width = width + 0.2
        self.length = length+0.2
        Ax = (self.centerX+(self.length/2))
        Ay = (self.centerY+(self.width/2))
        Bx = (self.centerX+(self.length/2))
        By = (self.centerY-(self.width/2))
        Cx = (self.centerX-(self.length/2))
        Cy = (self.centerY-(self.width/2))
        Dx = (self.centerX-(self.length/2))
        Dy = (self.centerY+(self.width/2))
        self.polygon = Polygon(
            [(Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), (Ax, Ay)])
        self.corners = [(Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy)]


maze = [Wall(-5.191, 0.9886, 1, 0.15), Wall(-5.639, -0.8309, 0.15, 3.769200), Wall(-5.672, 1.785, 0.15, 1.597130), Wall(-4.957, 2.543, 1.597130, 0.15), Wall(-4.277, 2.007956, 0.15, 1.169920), Wall(-0.0037, 2.51, 8.729630, 0.15), Wall(-1.588, 1.8136, 0.15, 1.25), Wall(-1.588, 0.0886, 0.15, 2.5), Wall(-2.138, 1.26, 1.25, 0.15), Wall(-2.668, 0.7136, 0.15, 1.25), Wall(-3.488, 0.16, 1.75, 0.15), Wall(2.405, 0.656, 0.75, 0.15), Wall(2.705, 0.956, 0.15, 0.75), Wall(3.2522, 1.2566, 1.25, 0.15), Wall(3.80526, 0.2066, 0.15, 2.25), Wall(3.3802, -0.844, 1, 0.15), Wall(2.955, -0.5433, 0.15, 0.75), Wall(2.7802, -0.2433, 0.5, 0.15), Wall(2.605, -0.5433, 0.15, 0.75), Wall(4.301, 2.189, 0.15, 0.810003), Wall(4.975, 2.5196, 1.50, 0.15), Wall(5.711,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              1.998, 0.15, 1.192330), Wall(5.306, 1.463, 0.919672, 0.15), Wall(5.698, 0.301, 0.15, 2.276490), Wall(5.185, -0.885, 1.119670, 0.15), Wall(4.7, -1.296, 0.15, 0.982963), Wall(5.67, -1.7033, 0.15, 1.75), Wall(5.154, -2.521, 1.185380, 0.15), Wall(0.673, -2.534, 7.883080, 0.15), Wall(1.906, -1.93, 0.15, 1.206910), Wall(0.877, -1.7, 0.15, 1.719980), Wall(0.2502, -0.917, 1.50, 0.15), Wall(-0.433, -1.389, 0.15, 1.072), Wall(-0.4292, -0.4799, 0.15, 0.927565), Wall(0.9177, 0.2156, 0.15, 2.416050), Wall(0.23527, 1.3486, 1.5, 0.15), Wall(-0.439, 1.048, 0.15, 0.75), Wall(-3.2627, -1.72, 0.15, 1.75), Wall(-3.883, -0.9203, 1.414750, 0.15), Wall(-3.9377, -2.52, 1.5, 0.15), Wall(-4.615, -2.157, 0.15, 0.870384), Wall(2.105, 1.58, 0.15, 2.15893)]
# To try checking out how the maze looks, uncomment the following
# display_maze = [Wall(-5.191, 0.9886, 1, 0.15), Wall(-5.639, -0.8309, 0.15, 3.769200), Wall(-5.672, 1.785, 0.15, 1.597130), Wall(-4.957, 2.543, 1.597130, 0.15), Wall(-4.277, 2.007956, 0.15, 1.169920), Wall(-0.0037, 2.51, 8.729630, 0.15), Wall(-1.588, 1.8136, 0.15, 1.25), Wall(-1.588, 0.0886, 0.15, 2.5), Wall(-2.138, 1.26, 1.25, 0.15), Wall(-2.668, 0.7136, 0.15, 1.25), Wall(-3.488, 0.16, 1.75, 0.15), Wall(2.405, 0.656, 0.75, 0.15), Wall(2.705, 0.956, 0.15, 0.75), Wall(3.2522, 1.2566, 1.25, 0.15), Wall(3.80526, 0.2066, 0.15, 2.25), Wall(3.3802, -0.844, 1, 0.15), Wall(2.955, -0.5433, 0.15, 0.75), Wall(2.7802, -0.2433, 0.5, 0.15), Wall(2.605, -0.5433, 0.15, 0.75), Wall(4.301, 2.189, 0.15, 0.810003), Wall(4.975, 2.5196, 1.50, 0.15), Wall(5.711, 1.998, 0.15, 1.192330), Wall(5.306, 1.463, 0.919672, 0.15), Wall(5.698, 0.301, 0.15, 2.276490), Wall(5.185, -0.885, 1.119670, 0.15), Wall(4.7, -1.296, 0.15, 0.982963), Wall(5.67, -1.7033, 0.15, 1.75), Wall(5.154, -2.521, 1.185380, 0.15), Wall(0.673, -2.534, 7.883080, 0.15), Wall(1.906, -1.93, 0.15, 1.206910), Wall(0.877, -1.7, 0.15, 1.719980), Wall(0.2502, -0.917, 1.50, 0.15), Wall(-0.433, -1.389, 0.15, 1.072), Wall(-0.4292, -0.4799, 0.15, 0.927565), Wall(0.9177, 0.2156, 0.15, 2.416050), Wall(0.23527, 1.3486, 1.5, 0.15), Wall(-0.439, 1.048, 0.15, 0.75), Wall(-3.2627, -1.72, 0.15, 1.75), Wall(-3.883, -0.9203, 1.414750, 0.15), Wall(-3.9377, -2.52, 1.5, 0.15), Wall(-4.615, -2.157, 0.15, 0.870384), Wall(2.105, 1.58, 0.15, 2.15893)]
# for wall in display_maze:
#     x, y = wall.polygon.exterior.xy
#     plt.plot(x, y)
# plt.show()


def isPointInObstacles(xCoord, yCoord):
    valid_point = False
    for wall in maze:
        if Point(xCoord, yCoord).within(wall.polygon):
            valid_point = True
            break
    return valid_point


def isValidPoint(parentNodeX, parentNodeY, childNodeX, childNodeY):
    valid_point = not isPointInObstacles(childNodeX, childNodeY)
    treeEdge = LineString(
        [(parentNodeX, parentNodeY), (childNodeX, childNodeY)])
    for wall in maze:
        i = 0
        while i < 3:
            wallEdge = LineString([wall.corners[i], wall.corners[i + 1]])
            if treeEdge.intersects(wallEdge):
                valid_point = False
            i += 1
    return valid_point
