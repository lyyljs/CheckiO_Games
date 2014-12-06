#!/usr/bin/env python
# coding:utf-8

class Friends(object):

    def __init__(self, connections):
        '''
        >>> f1 = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
        >>> f2 = Friends([{"1", "2"}, {"3", "1"}])
        '''
        self.connections = []
        for x in connections:
            if x not in self.connections:
                self.connections.append(x)
    
    def add(self, connection):
        '''
        >>> f = Friends([{"1", "2"}, {"3", "1"}])
        >>> f.add({"1", "3"})
        False
        >>> f.add({"4", "5"})
        True
        '''
        if connection in self.connections:
            return False
        else:
            self.connections.append(connection)
            return True
    
    def remove(self, connection):
        '''
        >>> f = Friends([{"1", "2"}, {"3", "1"}])
        >>> f.remove({"1", "3"})
        True
        >>> f.remove({"4", "5"})
        False
        '''
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        else:
            return False
    
    def names(self):
        '''
        >>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "d"}))
        >>> f.names() == {"a", "b", "c", "d"}
        True
        >>> f.remove({"d", "c"})
        True
        >>> f.names() == {"a", "b", "c"}
        True
        '''
        names_set = set()
        for name in self.connections:
            names_set = names_set | name
        return names_set
        
    def connected(self, name):
        '''
        >>> f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))
        >>> f.connected("nikola") == {"sophia"}
        True
        >>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}))
        >>> f.connected("a") == {"b", "c"}
        True
        >>> f.connected("d")
        set()
        >>> f.remove({"c", "a"})
        True
        >>> f.connected("c") == {"b"}
        True
        >>> f.remove({"c", "b"})
        True
        >>> f.connected("c")
        set()
        '''
        x_connection = set()
        x_name = {name, }
        for x in self.connections:
            if name in x:
                x_connection = x_connection | x.difference(x_name)
        return x_connection
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
