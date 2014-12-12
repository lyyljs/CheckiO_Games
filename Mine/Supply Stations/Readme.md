 “Do not let your fire go out, spark by irreplaceable spark in the hopeless swamps of the not-quite, the not-yet, and the not-at-all. Do not let the hero in your soul perish in lonely frustration for the life you deserved and have never been able to reach. The world you desire can be won. It exists.. it is real.. it is possible.. it's yours.”
-- "Atlas Shrugged" by Ayn Rand

We need to supply our new factory with four various resources from four different stations. For simplicity we will name them 1st, 2nd, 3rd and 4th resources (we can leave the rest up to your imagination). For this we will need to calculate four routes from the supply stations to the factory. Trucks will must deliver our supplies without stopping and we can not build several layers roads. So the truck routes should not intersect.

You are given a rectangular map divided by square cells. The map is represented as a sequence of strings, where:
- "." is a clear cell;
- "X" is an obstacle (forest, lake, etc);
- "1", "2", "3" or "4" are supply stations;
- "F" is a factory.

You are given a rectangular map divided by square cells. The map is represented as a sequence of strings, where:
- "N" north (up);
- "S" south (down);
- "E" east (right);
- "W" west (left);
A route will be represented as a string with these letters. The result should be as a sequence (list or tuple) of four routes from 1st to 4th.

supply-stations

For the given example (image) the result will be described as:

["NEEEESSSWS",
 "WSSSSSSSEEENNNNEN,
 "NNNNEE",
 "NNNNWWWW"]

Input: The map as a tuple of strings.

Output: The routes as a tuple/list of strings.

Example:

supply_routes(("..........",

               ".1X.......",

               ".2X.X.....",

               ".XXX......",

               ".X..F.....",

               ".X........",

               ".X..X.....",

               ".X..X.....",

               "..3.X...4.",

               "....X....."))


How it is used: This algorithm which you will write can serve as a foundation for software that designs circuit boards, or as a simple traffic management system.

Precondition:
All test cases are solvable.
5 ≤ len(the_map) ≤ 10
all(5 ≤ len(row) ≤ 10 for row in the_map)