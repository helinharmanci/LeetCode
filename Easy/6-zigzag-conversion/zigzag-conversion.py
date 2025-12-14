class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""
        string_lists = list()
        for i in range (0, numRows):
            st = ""
            string_lists.append(st)
        
        loop_number = int(len(s)/numRows)#3
        if loop_number < 1 or numRows==1 :
            string_lists[0] += s
            return string_lists[0]

        string_index = 0
        list_index = -1

        for i in range (0, loop_number):
            list_index += 1
            print("start of going down:")
            while list_index < numRows:
                if string_index == len(s):
                    break
                print(f"string index {string_index} is added to list index {list_index}")
                string_lists[list_index] += s[string_index]

                string_index += 1
                list_index += 1
            
            
            list_index -= 1
            print("start of going up")
            while list_index > 0:
                if string_index == len(s):
                    break
                print(f"string index {string_index} is added to list index {list_index-1}")
                string_lists[list_index-1] += s[string_index]
                list_index -= 1
                string_index += 1

        for i in range (0, numRows):
            result += string_lists[i]

        return result


        
                
                
