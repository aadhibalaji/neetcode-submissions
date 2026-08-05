class Solution {
    public boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < 9; i++) {
            Set<Character> cols = new HashSet<>();
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    continue;
                }

                if (cols.contains(board[i][j])) {
                    return false;
                }
                cols.add(board[i][j]);
            }
        } 


        for (int i = 0; i < 9; i++) {
            Set<Character> rows = new HashSet<>();
            for (int j = 0; j < 9; j++) {
                if (board[j][i] == '.') {
                    continue;
                }

                if (rows.contains(board[j][i])) {
                    return false;
                }
                rows.add(board[j][i]);
            }
        } 

        for (int square = 0; square < 9; square++) {
            Set<Character> sqrs = new HashSet<>();
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    int row = (square / 3) * 3 + i;
                    int col = (square % 3) * 3 + j;
                    if (board[row][col] == '.') {
                        continue;
                    }
                    if (sqrs.contains(board[row][col])) {
                        return false;
                    }

                    sqrs.add(board[row][col]);
                }
            }
        } 


        return true;

    }
}
