"""
Given a string, sort it in decreasing order based on the frequency of characters.
​
Example 1:
​
```plaintext
Input:
"free"
​
Output:
"eefr"
​
Explanation:
'e' appears twice while 'f' and 'r' appear once.
So 'e' must appear before 'f' and 'r'. Therefore, "eerf" is also a valid answer.
```
​
Example 2:
​
```plaintext
Input:
"dddbbb"
​
Output:
"dddbbb"
​
Explanation:
Both 'd' and 'b' appear three times, so "bbbddd" is also a valid answer.
Note that "dbdbdb" is incorrect, as the same characters must be together.
```
​
Example 3:
​
```plaintext
Input:
"Bbcc"
​
Output:
"ccBb"
​
Explanation:
"ccbB" is also a valid answer, but "Bbcc" is incorrect.
Note that 'B' and 'b' are treated as two different characters.
```
"""
def frequency_sort(s: str) -> str:
    """
    Inputs:
    s -> str
​
    Output:
    str
    """
    # Your code here
    # why do we need a hash table for this problem?
    # this problem needs us to count up the number of occurrences of _something_ 
    
    # count up the occurrences of each letter in the input string
    counts = {}
    output = []
​
    for letter in s:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
​
    # sort the key-value pairs by their occurrences 
    # put the key-value pairs from the dict into a list 
    kv_pairs = counts.items()
    # sort the array by the values 
    sorted_pairs = sorted(kv_pairs, key=lambda x: x[1], reverse=True)
​
    # loop through our sorted pairs 
    # for each pair 
    for letter, frequency in sorted_pairs:
        # duplicate the letter frequency times 
        output.append(letter * frequency)
​
    return ''.join(output)
​
print(frequency_sort("free"))