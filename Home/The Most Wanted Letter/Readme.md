<div class="task-description-text">
                        <p>
    You are given a text, which contains different english letters and punctuation symbols.
    You should find the most frequent letter in the text. The letter returned must be in lower case.<br>
    While checking for the most wanted letter, casing does not matter, so for the purpose of your search,
    "A"&nbsp;==&nbsp;"a".
    Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
</p>
<p>
    If you have <strong>two or more letters with the same frequency</strong>,
    then return the letter which comes first in the latin alphabet.
    For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
</p>


<p>
    <strong>Input: </strong> A text for analysis as a string (unicode for py2.7).
</p>

<p>
    <strong>Output: </strong> The most frequent letter in lower case as a string.
</p>

<div class="for_info_only">
    <p>
        <strong>Example:</strong>
    </p>
    <pre class="brush: python">
checkio("Hello World!") == "l"
checkio("How do you do?") == "o"
checkio("One") == "e"
checkio("Oops!") == "o"
checkio("AAaooo!!!!") == "a"
checkio("abe") == "a"
</pre>
</div>

<p class="for_info_only">
    <strong>How it is used: </strong>
    For most decryption tasks you need to know the frequency of occurrence for various letters in a section of text.
    For example: we can easily crack a simple addition or substitution cipher if we know the frequency in which letters appear.
    This is interesting stuff for language experts!
</p>


<p><strong>Precondition</strong>:<br>
    A text contains only ASCII symbols.<br>
    0 &lt; len(text) &le; 10<sup>5</sup>
</p>

</div>
