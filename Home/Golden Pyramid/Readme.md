<div class="task-description-text">
                        <p>
    Our Robo-Trio need to train for future journeys and treasure hunts.
    Stephan has built a special flat model of a pyramid. Now the robots can train for speed gold running.
    They start at the top of the pyramid and must collect gold in each room,
    choose to take the left or right path and continue down to the next level.
    To optimise their gold runs, Stephan need to know the maximum amount of gold that can be collected in one run.
</p>
<p>
    Consider a tuple of tuples in which the first tuple has one integer and each consecutive tuple has one more integer
    then the last. Such a tuple of tuples would look like a triangle.
    You should write a program that will help Stephan find the highest possible sum on the most profitable route down the pyramid.
    All routes down the pyramid involve stepping down and to the left or down and to the right.

</p>
<p>
    <strong>Tips:</strong>
    Think of each step down to the left as moving to the same index location or to the right as one index location higher.
    Be very careful if you plan to use recursion here.
</p>
<p class="for_info_only" style="text-align: center">
    <img title="sum-in-triangles"
         src="https://checkio.s3.amazonaws.com/task/media/621648eec98a48f1a2e71f8b581289c8/sum-in-triangles.png"
         alt="sum-in-triangles"
         width="500px"/>
</p>
<p class="for_editor_only" style="text-align: center">
    <img title="sum-in-triangles"
         src="https://checkio.s3.amazonaws.com/task/media/621648eec98a48f1a2e71f8b581289c8/sum-in-triangles.png"
         alt="sum-in-triangles"
         width="380px"/>
</p>

<p><strong>Input: </strong>A pyramid as a tuple of tuples. Each tuple contains integers.</p>

<p><strong>Output: </strong>The maximum possible sum as an integer.</p>

<div class="for_info_only">
    <p><strong>Example:</strong></p>
<pre class="brush: python">count_gold((
    (1,),
    (2, 3),
    (3, 3, 1),
    (3, 1, 5, 4),
    (3, 1, 3, 1, 3),
    (2, 2, 2, 2, 2, 2),
    (5, 6, 4, 5, 6, 4, 3)
)) == 23
count_gold((
    (1,),
    (2, 1),
    (1, 2, 1),
    (1, 2, 1, 1),
    (1, 2, 1, 1, 1),
    (1, 2, 1, 1, 1, 1),
    (1, 2, 1, 1, 1, 1, 9)
)) == 15
count_gold((
    (9,),
    (2, 2),
    (3, 3, 3),
    (4, 4, 4, 4)
)) == 18
</pre>
</div>


<p class="for_info_only">
    <strong>How it is used: </strong>
    This is a classical problem which shows you how to use dynamic programming.
    This concept is a core component of many optimisation tasks.
</p>

<p>
    <strong>Precondition: </strong>
    0 &lt; len(pyramid) &le; 20<br>
    all(all(0 &lt; x &lt; 10 for x in row) for row in pyramid)
</p>

  </div>
