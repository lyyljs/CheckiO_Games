#!/usr/bin/env python
# coding:utf-8

class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        '''
        >>> Building(10, 10, 1, 2, 2)
        Building(10, 10, 1, 2, 2)
        >>> Building(0, 0, 10.5, 2.546)
        Building(0, 0, 10.5, 2.546, 10)
        '''
        self._south = south
        self._west = west
        self._width_WE = width_WE
        self._width_NS = width_NS
        self._height = height
#        raise NotImplementedError

    def corners(self):
        '''
        >>> Building(1, 2, 2, 2).corners() == {"north-west": [3, 2], "north-east": [3, 4], "south-west": [1, 2], "south-east": [1, 4]}
        True
        '''
        dict = {"north-west": [self._south + self._width_NS, self._west]}
        dict["north-east"] = [self._south + self._width_NS, self._west + self._width_WE]
        dict["south-west"] = [self._south, self._west]
        dict["south-east"] = [self._south, self._west + self._width_WE]
        self._corners = dict
        return self._corners
#        raise NotImplementedError

    def area(self):
        '''
        >>> Building(1, 2.5, 4.2, 1.25).area()
        5.25
        '''
        self._area = self._width_NS * self._width_WE
        return self._area
#        raise NotImplementedError

    def volume(self):
        '''
        >>> Building(1, 2.5, 4.2, 1.25, 101).volume()
        530.25
        '''
        self._volume = self.area() * self._height
        return self._volume
#        raise NotImplementedError

    def __repr__(self):
        '''
        >>> str(Building(0, 0, 10.5, 2.546)) == "Building(0, 0, 10.5, 2.546, 10)"
        True
        '''
        return ("Building(%s, %s, %s, %s, %s)" % (str(self._south), str(self._west), str(self._width_WE), str(self._width_NS), str(self._height))) 
#        raise NotImplementedError


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
#    import doctest
#    doctest.testmod()
#    '''
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
#    '''
