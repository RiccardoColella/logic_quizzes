import math


def theta(p):
    """ Calculates the theta angle of the given point p

    :param p: the point that needs his theta angle to be calculated
    :return: the theta angle calculated given the point p, the starting point P0 and the horizon
    """
    return math.atan2(p[1] - P0[1], p[0] - P0[0])


def distance(p):
    """ Calculates the distance between the given point and the starting one

    :param p: point that needs his distance to be calculated
    :return: the distance between the point p and the starting point P0
    """
    return math.sqrt((p[1] - P0[1]) ** 2 + (p[0] - P0[0]) ** 2)


def judge(p1, p2, p3):
    """ Judges if the point p1 must take place of the point p2 within the hull

    :param p1: the new point to be considered
    :param p2: the last point of the hull
    :param p3: the second-last point of the hull
    :return: True if p1 must take place of p2 within the hull
    """
    return (p2[0] - p3[0]) * (p1[1] - p3[1]) - (p2[1] - p3[1]) * (p1[0] - p3[0])


def MergeSort(points, result, begin, end):
    """ Merge sort algorithm based on theta and their distance

    :param points: list of points to be sorted
    :param result: variable that will contains the sorted points
    :param begin: first point that needs to be sorted
    :param end: last point that needs to be sorted
    :return:
    """
    if begin >= end:
        return

    mid = (end - begin) // 2 + begin
    begin_1, end_1 = begin, mid
    begin_2, end_2 = mid + 1, end

    MergeSort(points, result, begin_1, end_1)
    MergeSort(points, result, begin_2, end_2)

    k = begin
    while begin_1 <= end_1 and begin_2 <= end_2:
        if theta(points[begin_1]) < theta(points[begin_2]):
            result[k] = points[begin_1]
            begin_1 = begin_1 + 1
            k = k + 1
        elif theta(points[begin_1]) == theta(points[begin_2]):
            if distance(points[begin_1]) > distance(points[begin_2]):
                result[k] = points[begin_1]
                begin_1 = begin_1 + 1
                k = k + 1
            else:
                # result[k] = points[begin_2]
                begin_2 = begin_2 + 1
                # k = k+1
        else:
            result[k] = points[begin_2]
            begin_2 = begin_2 + 1
            k = k + 1

    while begin_1 <= end_1:
        result[k] = points[begin_1]
        begin_1 = begin_1 + 1
        k = k + 1

    while begin_2 <= end_2:
        result[k] = points[begin_2]
        begin_2 = begin_2 + 1
        k = k + 1

    for k in range(begin, end + 1):
        points[k] = result[k]


# -------------------- Graham's Scan Algorithm -------------------- #
def graham_scan(points):
    """ Graham's Scan Algorithm implementation

    :param points: points to be considered by the algorithm
    :return: a list containing the points that are part of the convex hull
    """
    global start
    start = None

    # find first points (bottommost + leftmost)
    for i, (x, y) in enumerate(points):
        if start is None or y < start[1]:
            start = points[i]
        if start[1] == y and start[0] > x:
            start = points[i]

    # remove start point form the points group
    del points[points.index(start)]

    # sort the points by theta and distance
    result = len(points) * [None]
    MergeSort(points, result, 0, len(points) - 1)

    # Graham's Scan Algorithm
    hull = [start, points[0]]
    for p in (points[1:]):
        while judge(p, hull[-1], hull[-2]) <= 0:
            del hull[-1]
        hull.append(p)

    return hull


def open_file(filename):
    """ This functions open the file containings the points and returns the list of points

    :param filename: name or path to the file to be opened
    :return: the list of points
    """
    my_file = open(filename, "r")
    content_list = my_file.readline()
    points_as_string_list = content_list.split(" ")
    points_retrieved = []
    for point in points_as_string_list:
        point = point.replace("(", "")
        point = point.replace(")", "")
        point = point.split(",")
        points_retrieved.append([int(point[0]), int(point[1])])

    return points_retrieved


def find_start(points):
    """ Given a number of points this function finds the lowest leftmost point that will be the start for the Graham's
    algorithm

    :param points: list of points
    :return: the lowest and leftmost point
    """
    min_x = 999999
    min_y = 999999
    for y in points:
        if y[1] < min_y:
            min_y = y[1]
    for x in points:
        if x[1] == min_y and x[0] < min_x:
            min_x = x[0]

    P0 = [min_x, min_y]
    return P0


if __name__ == '__main__':
    # generate points
    pts = open_file("points.txt")
    P0 = find_start(pts)
    # calculate convex hull by using graham scan
    hull = graham_scan(pts)

    print("The hull is composed by this number of points:", len(hull))
