# by using iterative approach of the pascal's triangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # pre-build the list
        pascal_triangle = [[] for _ in range(numRows)]

        for row in range(numRows):
            pascal_triangle[row] = [1] * (row+1)
            for col in range(1,row):
                pascal_triangle[row][col] = (pascal_triangle[row-1][col-1] + pascal_triangle[row-1][col])
        return pascal_triangle



# by using recursion and memoization we can achieve this state also, it's taking o(n^2).
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # using recursion
        def row_builder(row):
            if row == 0:
                return [[1]]
            triangle = row_builder(row-1)
            prev = triangle[-1]
            next_row = [1] +  [prev[i]+ prev[i+1] for i in range(len(prev)-1)] + [1]
            triangle.append(next_row)
            return triangle

        return row_builder(numRows-1)