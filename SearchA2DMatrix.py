def searchMatrix(self, matrix, target):
    if matrix == None or len(matrix) == 0:
        return False
    row = len(matrix)
    col = len(matrix[0])
    start, end = 0, row * col - 1 
    while start + 1 < end:
        mid = int(start + (end - start)/2)
        if matrix[int(mid/col)][mid%col] < target:
            start = mid
        else: 
            end = mid

    if matrix[int(start/col)][start%col] == target:
        return True
    if matrix[int(end/col)][end%col] == target:
        return True

    return False
