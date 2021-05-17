
def lengthOfLongestSubstring(s):
    
    max_length = start = 0
    map = {}
    
    for i in range(len(s)):
        if s[i] in map and start <= map[s[i]]:
            start = map[s[i]] + 1
        else:
            max_length = max(max_length, i-start+1)
        map[s[i]] = i
    return(max_length)

lengthOfLongestSubstring("banana")