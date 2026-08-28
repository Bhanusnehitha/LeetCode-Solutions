class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix=strs[0]

        for string in strs[1:]:
            
            while not string.startswith(prefix):

                prefix=prefix[ :-1]
        
        return prefix