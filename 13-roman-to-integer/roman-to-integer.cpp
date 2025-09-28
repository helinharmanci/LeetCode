#include <stack>

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> values = {
            {'I', 1}, {'V', 5}, {'X', 10},
            {'L', 50}, {'C', 100},
            {'D', 500}, {'M', 1000}
        };
        int sum = 0;
        for (int i = 0; i < s.size(); i++) {
            if (i + 1 < s.size() && values[s[i]] < values[s[i + 1]]) {
                sum -= values[s[i]];
            } else {
                sum += values[s[i]];
            }
        }
        return sum;
    }
};