'''
345. Reverse Vowels of a String
Easy
Topics
Companies
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"
'''

s = "leetcode"

sList = list(s)

i = 0
j = len(s)-1
vowelList = ['a','e','i','o','u']
while j > i:
    if sList[i] in vowelList or sList[i].lower() in vowelList:
        if sList[j] in vowelList or sList[j].lower() in vowelList:
            sList[i], sList[j] = sList[j], sList[i]
            i += 1
            j -= 1
        else:
            j -= 1
    else:
        i += 1

result = "".join(sList)
print(result)
