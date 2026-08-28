class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq={}

        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1

        sorted_chars=sorted(freq,key=freq.get,reverse=True)

        result = ""

        for ch in sorted_chars:
            result += ch * freq[ch]

        return result