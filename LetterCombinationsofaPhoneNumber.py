class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict1 = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", 
        '8':"tuv", '9':"wxyz"}
        cmb=[''] if digits else []
        for d in digits:
            cmb= [p+q for q in dict1[d] for p in cmb]
        return cmb
        