"""
You are given a non-empty list of words.
​
Write a function that returns the *k* most frequent elements.
​
The list that you return should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical
order should come first.
​
Example 1:
​
```plaintext
Input:
words = ["lambda", "school", "rules", "lambda", "school", "rocks", "z", "z"]
k = 3
​
Output:
["lambda", "school", "z"]
​
Explanation:
"lambda" and "school" are the two most frequent words.
```
​
Example 2:
​
```plaintext
Input:
words = ["the", "sky", "is", "cloudy", "the", "the", "the", "cloudy", "is", "is"]
k = 4
​
Output:
["the", "is", "cloudy", "sky"]
​
Explanation:
"the", "is", "cloudy", and "sky" are the four most frequent words. The words
are sorted from highest frequency to lowest.
```
​
Notes:
​
- `k` is always valid: `1 <= k <= number of unique elements.
- words in the input list only contain lowercase letters.
```
"""
def top_k_frequent(words, k):
    """
    Input:
    words -> List[str]
    k -> int
​
    Output:
    List[str]
    """
    # Your code here
    counts = {}
​
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
​
    # sort the words in descending order by their occurrences 
    kv_pairs = counts.items()
​
    sorted_pairs = sorted(kv_pairs, key=lambda x: (-x[1], x[0]))
    top_k = sorted_pairs[:k]
​
    return [word for word, freq in top_k]
​
print(top_k_frequent(["lambda", "z", "z", "school", "rules", "lambda", "school", "rocks"], 3))