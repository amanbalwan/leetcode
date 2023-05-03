class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s=[]
        intervals.sort()
        s
    
        for i in range(len(intervals)):
            if s==[]:
                s.append(intervals[i])
            else:
                prevend=s[-1][1]
                end=intervals[i][1]
                start=intervals[i][0]
                if prevend>=start:
                    s[-1][1]=max(prevend,end)
                else:
                    s.append(intervals[i])
                
            
                
                
        return s
            
            
            
            
        