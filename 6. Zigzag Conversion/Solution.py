class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
           

        rows = [''] * numRows
        current_row = 0
        going_down = False  # To track the direction of movement in the zigzag pattern

        for char in s:
        # Place character in the current row
            rows[current_row] += char
        
        # Decide whether to go up or down
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
        
        # Update the current row we're filling
            if going_down:
                current_row += 1
            else:
                current_row -= 1

    # Combine all rows to form the final string
        return ''.join(rows)


    