The robots have learned that the last container which they picked up during a supply stop on another island is radioactive. There are five different kinds of spare parts contained within marked by number. The radiation is emitted from the largest group of identical spare parts (where each part is adjacently joined). Help them find this group and point out the quantity of identical parts within the group as well as the number of the spare part itself in the container.

The container is represented as a square matrix. The numbers 1 through 5 are used to label the different kinds of spare parts -- the elements of the matrix. Zero is an empty cell. Find the largest group of identical numbers adjacently joined to each other and point out both the quantity of the spare parts within the group and the number of the spare part itself.

radiation_search

Input: A square matrix as a list of lists. Each list contains integers

Output: The size and marking of the largest group as a list of two integers.

Example:

checkio([

    [1, 2, 3, 4, 5],

    [1, 1, 1, 2, 3],

    [1, 1, 1, 2, 2],

    [1, 2, 2, 2, 1],

    [1, 1, 1, 1, 1]]) == [14, 1]

​

checkio([

    [2, 1, 2, 2, 2, 4],

    [2, 5, 2, 2, 2, 2],

    [2, 5, 4, 2, 2, 2],

    [2, 5, 2, 2, 4, 2],

    [2, 4, 2, 2, 2, 2],

    [2, 2, 4, 4, 2, 2]]) == [19, 2]


How it is used: In this task, you can learn about Union-finding algorithms and Disjoint-set data structures. It can be used in image recognition, geographic analysis and even model the partitioning of a set.

Precondition:
3 ≤ len(matrix) ≤ 10
all(all(0 ≤ x ≤ 5 for x in row) for row in matrix
any(any(x for x in row) for row in matrix
The tests have only one unique solutions.
