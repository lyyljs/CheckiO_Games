<div class="task-description-text">
 <div class="story">
  <p>
   "Animals and plants can reproduce themselves,
   but it was only recently shown that machines can be made which also
   reproduce themselves……. Other kinds of self-reproducing machines
   will be described, and one simple mechanical
   model, with no electrical or magnetic complications,
   will be there in working order for the audience to inspect and operate."
  </p>
  <p>
   -- Edward Forrest Moore
  </p>
 </div>

<p>
    In cellular automata, <a href="http://en.wikipedia.org/wiki/Moore_neighborhood">the
    Moore neighborhood</a> comprises
    the eight cells surrounding a central cell on a two-dimensional square lattice.
    The neighborhood is named after Edward F. Moore, a pioneer of cellular automata theory.
    Many board games are played with a rectangular grid with squares as cells.
    For some games, it is important to know about the conditions of neighbouring cells for chip
    (figure, draught etc) placement and strategy.
</p>

<p>
    You are given a state for a rectangular board game grid with chips in a binary matrix, where 1
    is a cell with a chip and 0 is an empty cell. You are also given the coordinates for a cell in
    the form of row and column numbers (starting from 0). You should determine how many chips are
    close to this cell. Every cell interacts with its eight neighbours; those cells that are
    horizontally, vertically, or diagonally adjacent.
</p>

<p style="text-align: center;">
    <img title="example" src="https://checkio.s3.amazonaws.com/task/media/9666d6bd6e5b4a3aa30825bedf7d5b59/example.svg" alt="example"
         style="max-width: 520px;width: 100%;"/>
</p>

<p>
    For the given examples (see the schema) there is the same grid:
</p>
<pre>
((1, 0, 0, 1, 0),
 (0, 1, 0, 0, 0),
 (0, 0, 1, 0, 1),
 (1, 0, 0, 0, 0),
 (0, 0, 1, 0, 0),)
</pre>
<br>
<p>
    For the first example coordinates of the cell is (1,&nbsp;2) and
    as we can see from the schema this
    cell has 3 neighbour chips.
    For the second example coordinates is (0,&nbsp;0) and this cell contains
    a chip, but we count only neighbours and the answer is 1.
</p>
<p>
    <strong>Input: </strong> Three arguments. A grid as a tuple of tuples with integers (1/0),
    a row number and column number for a cell as integers.
</p>

<p>
    <strong>Output: </strong> How many neighbouring cells have chips as an integer.
</p>


<div class="for_info_only">
    <p>
        <strong>Example:</strong>
    </p>
    <pre class="brush: python">
count_neighbours(((1, 0, 0, 1, 0),
                  (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 1),
                  (1, 0, 0, 0, 0),
                  (0, 0, 1, 0, 0),), 1, 2) == 3
count_neighbours(((1, 0, 0, 1, 0),
                  (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 1),
                  (1, 0, 0, 0, 0),
                  (0, 0, 1, 0, 0),), 0, 0) == 1</pre>
</div>
<br>
<p class="for_info_only">
    <strong>How it is used: </strong>
    As we mentioned in the beginning, this idea can be useful for developing board game algorithms.
    In addition, the same principles it can be useful for navigational software, or geographical
    surveying software.

</p>

<p>
    <strong>Precondition:</strong><br>
    3 &le; len(grid) &le; 10<br>
    all(len(grid[0]) == len(row) for row in grid)
</p>
</div>
