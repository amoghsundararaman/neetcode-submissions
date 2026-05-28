class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find_ele(count_ele: int, matrix: List[List[int]], cn: int):
            r = count_ele // cn
            c = count_ele % cn
            return matrix[r][c]
        row_count, column_count = len(matrix), len(matrix[0])
        total_ele = row_count * column_count
        low, hi = 0, total_ele - 1

        while low <= hi: 
            mid = low + (hi - low) // 2
            mid_ele = find_ele(mid, matrix, column_count)

            if mid_ele == target: 
                return True
            elif mid_ele > target: 
                hi = mid - 1
            else: 
                low = mid + 1
        return False




        