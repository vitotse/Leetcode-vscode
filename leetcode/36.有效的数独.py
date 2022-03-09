#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_map = [dict() for _ in range(9)]
        cols_map = [dict() for _ in range(9)]
        boxes_map = [dict() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                num = int(board[i][j])
                box_index = (i // 3) * 3 + j // 3
                row_num = rows_map[i].get(num, 0)
                col_num = cols_map[j].get(num, 0)
                box_num = boxes_map[box_index].get(num, 0)

                if row_num > 0 or col_num > 0 or box_num > 0:
                    return False

                rows_map[i][num] = 1
                cols_map[j][num] = 1
                boxes_map[box_index][num] = 1
        return True



# @lc code=end

