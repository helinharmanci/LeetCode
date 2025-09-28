class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int i = 0; i < 9; i++) {
            vector<bool> seen(9, false);
            for (int j = 0; j < 9; j++) {
                char c = board[i][j];
                if (c == '.') continue;
                int idx = c - '1';
                if (seen[idx]) return false;
                seen[idx] = true;
            }
        }

        for (int j = 0; j < 9; j++) {
            vector<bool> seen(9, false);
            for (int i = 0; i < 9; i++) {
                char c = board[i][j];
                if (c == '.') continue;
                int idx = c - '1';
                if (seen[idx]) return false;
                seen[idx] = true;
            }
        }
        
        for (int blockRow = 0; blockRow < 3; blockRow++) {
        for (int blockCol = 0; blockCol < 3; blockCol++) {
            vector<bool> seen(9, false);
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    char c = board[blockRow*3 + i][blockCol*3 + j];
                    if (c == '.') continue;
                    int idx = c - '1';
                    if (seen[idx]) return false;
                    seen[idx] = true;
                }
            }
        }
    }

        return true;
    }
};