class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s=[]
        i=0
        while i<len(intervals):
            if newInterval[0]<=intervals[i][1]:
                if newInterval[1]<intervals[i][0]:
                    break
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            else:
                s.append(intervals[i])
            i+=1
        s.append(newInterval)
        s+=intervals[i:]
        return s
        