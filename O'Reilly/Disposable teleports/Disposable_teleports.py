#!/usr/bin/env python
#coding:utf-8

def route_search(station, route, teleports, used_teleports):
    global result
    if result != "":
        return
    for teleport in teleports:
        if station in teleport and teleport not in used_teleports:
            used_teleports.append(teleport)
            next_station = list(teleport.difference(station))[0]
            route += next_station
            if len(set(route)) == 8 and next_station == '1':
                result = route
                return
            route_search(next_station, route, teleports, used_teleports)
            used_teleports.pop()
            route = route[:-1]

def checkio(teleports_string):
    #return any route from 1 to 1 over all points
    global result
    result = ""
    teleports = list()
    for teleport in teleports_string.split(','):
        teleports.append(set(teleport))
    route_search('1', '1', teleports, [])
    return result

#This part is using only for self-testing
if __name__ == "__main__":
    def check_solution(func, teleports_str):
        route = func(teleports_str)
        teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
        if route[0] != '1' or route[-1] != '1':
            print("The path must start and end at 1")
            return False
        ch_route = route[0]
        for i in range(len(route) - 1):
            teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
            if not teleport in teleports_map:
                print("No way from {0} to {1}".format(route[i], route[i + 1]))
                return False
            teleports_map.remove(teleport)
            ch_route += route[i + 1]
        for s in range(1, 9):
            if not str(s) in ch_route:
                print("You forgot about {0}".format(s))
                return False
        return True

    assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
    assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
    assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"
