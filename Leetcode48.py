
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        pos1,pos2 = 0,len(matrix)-1
        while   pos1<pos2:
            add = 0
            while   add < pos2-pos1:
                #左上角为0块，右上角为1块，右下角为2块，左下角为3块
                temp = matrix[pos2-add][pos1]
                matrix[pos2-add][pos1] = matrix[pos2][pos2-add]
                #3 = 2
                matrix[pos2][pos2-add] = matrix[pos1+add][pos2]
                #2 = 1
                matrix[pos1+add][pos2] = matrix[pos1][pos1+add]
                #1 = 0
                matrix[pos1][pos1+add] = temp
                #0 = temp
                add = add+1
            pos1 = pos1+1
            pos2 = pos2-1