 For language training our Robots want to learn about suffixes.

In this task, you are given a set of words in lower case. Check whether there is a pair of words, such that one word is the end of another (a suffix of another). For example: {"hi", "hello", "lo"} -- "lo" is the end of "hello", so the result is True.

Input: Words as a set of strings.

Output: True or False, as a boolean.

Example:

checkio({"hello", "lo", "he"}) == True

checkio({"hello", "la", "hellow", "cow"}) == False

checkio({"walk", "duckwalk"}) == True

checkio({"one"}) == False

checkio({"helicopter", "li", "he"}) == False


How it is used: Here you can learn about iterating through set type and string data type functions.

Precondition: 2 ≤ len(words) < 30
all(re.match(r"\A[a-z]{1,99}\Z", w) for w in words)

Each player can create their own missions on CheckiO starting at level 9. You have the ability to create challenges for your friends and maybe even get your mission published on CheckiO for the whole community!
 
