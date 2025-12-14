class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_list = sorted(strs, key=len)
        smallest_str = sorted_list[0]

        for one_str in sorted_list:
            
            if one_str.startswith(smallest_str):
                continue
            else:
                while(not (one_str.startswith(smallest_str))):
                    length = len(smallest_str)
                    smallest_str = smallest_str[0:(length-1)]
                    
        
        return smallest_str
        