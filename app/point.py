
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x: %s, y: %s' % (self.x, self.y)
    
    def __repr__(self):
        return self.__str__()

class Vector(object):
    def __init__(self, start, stop):
        """
        start, stop - point (x, y)
        """
        self.start = start
        self.stop = stop
        try:
            self.dx = stop.x - start.x
            self.dy = stop.y - start.y
        except:
            self.dx = stop[0] - start[0]
            self.dy = stop[1] - start[1]

    def __str__(self):
        return 'dx: %s, dy: %s' % (self.dx, self.dy)

    def __repr__(self):
        return self.__str__()



