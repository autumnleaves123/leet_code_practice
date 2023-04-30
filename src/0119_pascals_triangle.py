class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # completed on 4/30/2023. Redid my first solution to account for symmetry
        
        tri = []

        curRow = 1

        while curRow <= numRows:

            # initialize current row with all 1's because first and last element of each row is 1
            row = [1]*curRow
            i = 1

            while i < curRow/2:
                # each row starts and ends with 1
                row[i] = tri[-1][i-1] + tri[-1][i]
                row[-i-1] = row[i]
                i+=1
            
            # add finished row to triangle
            tri.append(row)
            # increment row
            curRow+=1
        
        return tri