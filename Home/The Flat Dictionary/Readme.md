<div class="task-description-text">
                        <p>
    Nikola likes to categorize everything in sight.
    One time Stephan gave him a label maker for his birthday,
    and the robots were peeling labels off of every surface in the ship for weeks.
    He has since categorized all the reagents in his laboratory,
    books in the library and notes on the desk.
    But then he learned about python <a href="https://docs.python.org/3/library/stdtypes.html#mapping-types-dict">dictionaries</a>,
    and categorized all the possible configurations for Sophia’s drones.
    Now the files are organized in a deep nested structure,
    but Sophia doesn’t like this. Let's help Sophia to flatten these dictionaries.
</p>

<p>
    Python dictionaries are a convenient data type to store and process configurations.
    They allow you to store data by keys to create nested structures.
    You are given a dictionary where the keys are strings and the values are strings or dictionaries.
    The goal is flatten the dictionary, but save the structures in the keys.
    The result should be the a dictionary without the nested dictionaries.
    The keys should contain paths that contain the parent keys from the original dictionary.
    The keys in the path are separated by a "/". If a value is an empty dictionary,
    then it should be replaced by an empty string (""). Let's look at an example:
</p>
<pre class="brush: python">
{
    "name": {
        "first": "One",
        "last": "Drone"
    },
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"}
    }
}
</pre>
<p>
    The result will be:
</p>
<pre class="brush: python">
{"name/first": "One",           #one parent
 "name/last": "Drone",
 "job": "scout",                #root key
 "recent": "",                  #empty dict
 "additional/place/zone": "1",  #third level
 "additional/place/cell": "2"}
</pre>

<p>
    Sophia has already written the code for this task, but it has a bug.

    <strong>You need to find and fix this bug.</strong>
</p>

<p>
    <strong>Input: </strong> An original dictionary as a dict.
</p>

<p>
    <strong>Output: </strong> The flattened dictionary as a dict.
</p>



<div class="for_info_only">
    <p>
        <strong>Example:</strong>
    </p>
    <pre class="brush: python">
flatten({"key": "value"}) == {"key": "value"}
flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {"key/deeper/more/enough": "value"}
flatten({"empty": {}}) == {"empty": ""}
    </pre>
</div>

<p class="for_info_only">
    <strong>How it is used: </strong>
    This concept can be useful if you need to parse config files and simplify structures
    for grandfathered systems and file structures.
    You can easily modify this idea for your own specifications.
    Besides that, it's a  useful skill to be able to read code and search for bugs.
</p>

<p>
    <strong>Precondition:</strong><br>
    <strong>Keys</strong> in a dictionary are non-empty strings.<br>
    <strong>Values</strong> in a dictionary are strings or dicts.<br>
    root_dictionary != {}<br>
</p>

</div>
