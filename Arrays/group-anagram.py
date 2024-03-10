class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for i in strs:
            sortedWord = ''.join(sorted(i))
            d.setdefault(sortedWord,[])
            d[sortedWord].append(i)     
        return d.values()

ans = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(ans)