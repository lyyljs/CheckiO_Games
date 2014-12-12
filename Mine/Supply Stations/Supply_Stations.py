#!/usr/bin/env python
#coding:utf-8

WAYS = (((1, 0), (0, 1), (0, -1), (-1, 0)), ((1, 0), (0, -1), (-1, 0), (0, 1)), 
    ((-1, 0), (0, 1), (1, 0), (0, -1)), ((0, -1), (-1, 0), (1, 0), (0, 1)))

SUPPLYS = ("1", "2", "3", "4")

DIRS = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1),
    }

MAX_COUNT = {1:500, 2:500, 3:500, 4:500}

def dir_to_f(pos):
    global pos_of_f
    if pos[0] < pos_of_f[0]:
        if pos[1] < pos_of_f[1]:
            return 0
        else:
            return 1
    else:
        if pos[1] < pos_of_f[1]:
            return 2
        else:
            return 3


def get_pos(supply, the_map):
    i = 0
    while i < len(the_map):
        try:
            return [i, the_map[i].index(supply)]
        except:
            i += 1

def getdir(way):
    for dir in DIRS:
        if DIRS[dir] == way:
            return dir

def route_search(supply, order, pos, route, deep):
    global got_result, map, opened, routes, count
    if got_result:
#        print("Got Result")
        return True
    n = len(map)
    m = len(map[0])
    if count[supply] > MAX_COUNT[supply]:
        return False
    dir_f = dir_to_f(pos)
    for t in WAYS[dir_f]:
        x, y = pos[0] + t[0], pos[1] + t[1]
        if x < 0 or y < 0 or x >= n or y >= m or map[x][y] == "X" or map[x][y] in SUPPLYS or opened[x][y] == 1:
            pass
        else:
            count[supply] += 1
            route += getdir(t)
            if map[x][y] == "F":
                routes.append(route)
#                print("got route :", order[supply - 1], "count :", count, ":", route)
                if supply == 4:
                    got_result = True
                    return True
                else:
                    next_supply = supply + 1
                    next_pos = get_pos(order[next_supply - 1], map)
                    route_search(next_supply, order, next_pos, "", 0)         
                if not got_result:
                    routes.pop()
                    count[next_supply] = 0
                return True
#            print(supply, "count :", count, ":", route)
            opened[x][y] = 1
            route_search(supply, order, [x, y], route, deep + 1)
            route = route[:-1]
            opened[x][y] = 0
    return False

def get_orders(deep, order, used):
    global orders
    i = 1
    while i < 5:
        if used[i]:
            pass
        else:
            used[i] = 1
            order += str(i)
            if deep < 4:
                get_orders(deep + 1, order, used)
            else:
                orders.append(order)
            order = order[:-1]
            used[i] = 0
        i += 1


def supply_routes(the_map):
    global got_result, map, opened, routes, pos_of_f, count, orders
    
    map = the_map
    got_result = False
    opened, routes, orders, used = [], [], [], []
    
    for x in range(len(the_map)):
        temp = []
        for y in range(len(the_map[0])):
            temp.append(0)
        opened.append(temp)
        
    pos_of_f = get_pos("F", the_map)
    
    for i in range(5):
        used.append(0)
    get_orders(1, "", used)
    
    for order in orders:
        count = {1:0, 2:0, 3:0, 4:0}
        for row in range(len(opened)):
            for col in range(len(opened[0])):
                opened[row][col] = 0
        t = get_pos(order[0], the_map)
        routes = []
        route_search(1, order, t, "", 0)
        if got_result:
            return routes[order.index("1")], routes[order.index("2")], routes[order.index("3")], routes[order.index("4")]
    return routes

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    def checker(f, the_map):
        result = f(the_map)
        if (not isinstance(result, (tuple, list)) and len(the_map) != 4 and
                any(not isinstance(r, str) for r in the_map)):
            return False, "The result must be a list/tuple of four strings"
        stations = [None] * 4
        factory_supply = [0] * 4
        for i, row in enumerate(the_map):
            for j, ch in enumerate(row):
                if ch in "1234":
                    stations[int(ch) - 1] = (i, j)
        wmap = [list(row) for row in the_map]
        width = len(wmap[0])
        height = len(wmap)
        for numb, route in enumerate(result, 1):
            coor = stations[numb - 1]
            for i, ch in enumerate(route):
                if ch not in DIRS.keys():
                    return False, "Routes must contain only NSWE"
                row, col = coor[0] + DIRS[ch][0], coor[1] + DIRS[ch][1]
                if not (0 <= row < height and 0 <= col < width):
                    return False, "Ooops, we lost the route from station {}".format(numb)
                checked = wmap[row][col]
                if checked == "X":
                    return False, "The route {} was struck {} {}".format(numb, coor, (row, col))
                if checked == "F":
                    factory_supply[numb - 1] = 1
                    if i >= len(route):
                        return False, "A route should be ended in the factory"
                    break
                if checked != ".":
                    return False, "Don't intersect routes"
                wmap[row][col] = str(numb)
                coor = row, col
        if factory_supply != [1, 1, 1, 1]:
            return False, "You should deliver all four resources"
        return True, "Great!"
    '''
    print(    supply_routes((
    "2.......",
    "X.XXX.X.",
    ".F..X.X.",
    "..X.X.X.",
    "1.3...X4",)))
                                    
    '''
    test1 = checker(supply_routes, ("..........",
                                    ".1X.......",
                                    ".2X.X.....",
                                    ".XXX......",
                                    ".X..F.....",
                                    ".X........",
                                    ".X..X.....",
                                    ".X..X.....",
                                    "..3.X...4.",
                                    "....X....."))
    print(test1[1])
    assert test1[0], "First test"
    test2 = checker(supply_routes, ("1...2",
                                    ".....",
                                    "..F..",
                                    ".....",
                                    "3...4"))
    print(test2[1])
    assert test2[0], "Second test"
    test3 = checker(supply_routes, ("..2..",
                                    ".....",
                                    "1.F.3",
                                    ".....",
                                    "..4.."))
    print(test3[1])
    assert test3[0], "Third test"
    test4 = checker(supply_routes, ("..........", 
                                    ".F..XXXXX.", 
                                    "..........", 
                                    ".X........", 
                                    ".X........", 
                                    ".X........", 
                                    ".X........", 
                                    ".X......4.", 
                                    ".X.....3X2", 
                                    "........1."))
    print(test4[1])
    assert test4[0], "Fourth test"
    test5 = checker(supply_routes, (".....", 
                                    "...X.", 
                                    "3F..1", 
                                    ".4.2.", 
                                    "....."))
    print(test5[1])
    assert test5[0], "Fifth test"
    test7 = checker(supply_routes, (
    "2.......",
    "X.XXX.X.",
    ".F..X.X.",
    "..X.X.X.",
    "1.3...X4",))
    print(test7[1])
    assert test7[0], "Seventh test"
    test6 = checker(supply_routes, (".....4...", 
                                    "....3F...", 
                                    ".........", 
                                    "XXXXXXX..", 
                                    "X.....X..", 
                                    "1........", 
                                    "2..X....."))
    print(test6[1])
    assert test6[0], "Sixth test"
#    '''
