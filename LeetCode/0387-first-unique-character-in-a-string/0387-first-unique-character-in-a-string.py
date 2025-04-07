class Solution(object):
    def firstUniqChar(self, s):
        
        char_list = []

        for i in range(len(s)):
            char = s[i]

            if char in char_list:
                continue
            else: 
                if char in s[i+1:]:
                    char_list.append(char)
                    continue
                else:
                    return i

        return -1