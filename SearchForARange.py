def searchRange(self, A, target):
    if A == None or len(A) == 0:
        return [-1, -1]
    first = self.findFirst(A, target)
    last = self.findLast(A, target)
    return [first, last]
        
    def findFirst(self, A, target):
        start, end = 0, len(A) - 1 
        while start + 1 < end:
            mid = int(start + (end - start)/2)
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        return -1
        
    def findLast(self, A, target):
        start, end = 0, len(A) - 1 
        while start + 1 < end:
            mid = int(start + (end - start)/2)
            if A[mid] > target:
                end = mid
            else:
                start = mid
        if A[end] == target:
            return end
        elif A[start] == target:
            return start
        return -1
