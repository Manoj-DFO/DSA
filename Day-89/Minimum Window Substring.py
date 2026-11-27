class Solution(object):
    def minWindow(self, s, t):
        
        if not s or not t:
            return ''

        dit = {}

        for i in t:
            dit[i] = dit.get(i, 0) + 1

        window = {}
        left = 0
        formed = 0
        required = len(dit)
        minimum = float('inf')

        for i in range(len(s)):
            
            ch = s[i]
            window[ch] = window.get(ch, 0) + 1

            if ch in dit and dit[ch] == window[ch]:
                formed += 1

            while required == formed:
                
                if i - left + 1 < minimum:
                    minimum = i - left + 1
                    start = left

                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in dit and window[left_ch] < dit[left_ch]:

                    formed -= 1

                left += 1

        if minimum == float("inf"):
            return ""

        return s[start:start + minimum]