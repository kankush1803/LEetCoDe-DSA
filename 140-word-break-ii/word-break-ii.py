class Solution:
    def wordBreak(self,s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        
    
    
        res=[]
        def solve(curr,s):
            if len(s)==0:
                res.append(curr.strip())
                return 


            for i in range(len(s)):
                lstr=s[0:i+1]
                if lstr in wordSet:
                    rstr=s[i+1:]

                    solve(curr +" "+ lstr ,rstr)
            
        solve("",s)
        return res
        