<div class="task-description-text">
                        <div class="story">
    <div style="text-align: center">
        <img src="https://checkio.s3.amazonaws.com/task/media/115c9e71decd4329a8df694808fa74d0/robots.png" width="600px">
    </div>
    <p>
        If you have 50 different plug types, appliances wouldn't be available and would be very
        expensive. But once an electric outlet becomes standardized, many companies can design
        appliances, and competition ensues, creating variety and better prices for consumers.
        <br>
        -- Bill Gates

    </p>

</div>

<p>
    You are given a non-empty list of integers (X).
    For this task, you should return a list consisting of only the non-unique elements in this list.
    To do so you will need to remove all unique elements (elements which are contained in a given
    list only once).
    When solving this task, do not change the order of the list.
    Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].

</p>

<p style="text-align: center;">
    <img class="for_info_only"
         title="non-unique-elements"
         src="https://checkio.s3.amazonaws.com/task/media/115c9e71decd4329a8df694808fa74d0/non-unique-elements.png"
         alt="non-unique-elements"
         width="600px"/>
    <img class="for_editor_only"
         title="non-unique-elements"
         src="https://checkio.s3.amazonaws.com/task/media/115c9e71decd4329a8df694808fa74d0/non-unique-elements.png"
         alt="non-unique-elements"
         width="380px"/>
</p>

<p><strong>Input: </strong>A list of integers.</p>

<p><strong>Output: </strong>The list of integers.</p>
<div class="for_info_only">
    <p><strong>Example:</strong></p>
<pre class="brush: python">checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
checkio([1, 2, 3, 4, 5]) == []
checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]</pre>
</div>
<br>
<p>
    <strong>How it is used:</strong>
    This mission will help you to understand how to manipulate arrays,
    something that is the basis for solving more complex tasks.
    The concept can be easily generalized for real world tasks.
    For example: if you need to clarify statistics by removing low frequency elements (noise).

</p>

<p><strong>Precondition:</strong><br>
    0 &lt; len(data) &lt; 1000<br>
</p>
</div>
