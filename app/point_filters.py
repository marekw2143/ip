"""
Provides functions for filtering odd points from sets of points defining regular shapes
"""


from point import Point, Vector
from pdb import set_trace
import math, logging


# create logger
log= logging.getLogger("simple_example")
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
log.addHandler(ch)



# average
avg = lambda L: sum(L)/len(L)

# odchylenie standardowe
_dev = lambda L, avg_: math.sqrt(sum([(el - avg_)**2 for el in L]))
dev = lambda L: _dev(L, avg(L))



# TODO: maybe add some regular shapes checking
def filter_odd_points2(points, A = 3, factor = 1.5):
    """
    points - list of Point class
    A - amount of points back and from that will be used to contstruct vectors to compare
    factor - vlaue that give vector will be multipled by to check if it's odd
    for each point:
        calculate vector with next point
        calculate vector with each A points next, and back (back are calculated - back first, then actual"
        calculate vectors between all points in A distance from actually processed vector (vectors in abs)
    """
    ret = []
    for i in range(len(points)):
        try:
            local_vectors = []

            # for each point that is A units far from i'th:
            for j in [tj for tj in range(i-A, i+A) if tj in range(len(points))]:
                # calculate vector between 2 points
                try:
                    added_vector = Vector(points[j], points[j+1])
                except:
                    log.debug("i: %s, j: %s" % (i, j))
                    break
                local_vectors.append(added_vector)
            checked_vector = Vector(points[i], points[i+1])

            # calculate statisctics on local vectors
            l_dx = [v.dx for v in local_vectors]
            l_dy = [v.dy for v in local_vectors]
            dev_dx = dev(map(abs, l_dx))
            dev_dy = dev(map(abs, l_dy))
            avg_dx = avg(l_dx)
            avg_dy = avg(l_dy)

            log.debug('''
    dev_dx: %s
    dev_dy: %s
    avg_dx: %s
    avg_dy: %s''' % (dev_dx, dev_dy, avg_dx, avg_dy))

            added = Point(points[i].x, points[i].y)
            if i > 0:
                # modify checked_vector - if dx or dy is different - simply add previous trend + average dx
                log.debug('checked_vector: %s' % checked_vector)
                if abs(checked_vector.dx) * factor > dev_dx: 
                    added.x = ret[len(ret) - 1].x + avg_dx
                if abs(checked_vector.dy) * factor > dev_dy:
                    added.y = ret[len(ret) - 1].y + avg_dy
            ret.append(added)
        except:
            return ret
    return ret

if __name__ == "__main__":
    points = [Point(x, x) for x in range(10)]
    points[4] = Point(20, 20)
    print points

    p2 = filter_odd_points2(points, 3)
    print p2
