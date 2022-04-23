# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
#########################################################################################


def anagram_checker(s: str, t: str):
    khali_dict = {}
    khali_dict2 = {}
    for ch in s:
        if ch not in khali_dict:
            khali_dict[ch] = 1
        else:
            khali_dict[ch] = khali_dict[ch] + 1
    for c in t:
        if c not in khali_dict2:
            khali_dict2[c] = 1
        else:
            khali_dict2[c] = khali_dict2[c] + 1
    if khali_dict == khali_dict2:
        return True
    else:
        return False


# driver code
if __name__ == "__main__":
    print(anagram_checker("aacc", "ccac"))
