class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        def row_builder(row):
            if row == 0:
                return [1]
            final_row = row_builder(row-1)
            new_row = [1] + [final_row[i] + final_row[i+1] for i in range(len(final_row) - 1)] + [1]
            return new_row
        return row_builder(rowIndex)


# using recursive call stack