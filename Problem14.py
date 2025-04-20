'''
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

def isAnagram(s, t):
    letter_count_arr = [0] * 26

    for ch in s:
        letter_count_arr[ord(ch) - ord('a')] += 1
    for ch in t:
        letter_count_arr[ord(ch) - ord('a')] -= 1
    
    for letter in letter_count_arr:
        if letter != 0:
            return False 
    return True

s = "anagram"
t = "nagaram"
result = isAnagram(s, t)
print(result)