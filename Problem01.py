'''

You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s


'''

word1 = "abcd"
word2 = "pq"

maxLen = max(len(word1), len(word2))
finalWord = []
for i in range(maxLen):
    print(word1[i])
    print(word2[i])
    finalWord.append(word1[i])
    finalWord.append(word2[i])

if(len(word1) > maxLen):
    finalWord.append(word1[maxLen:len(word1)])
elif(len(word2) > maxLen):
    finalWord.append(word2[maxLen:len(word2)])

print("".join(finalWord))
