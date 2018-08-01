 def minArea(self, image, x, y):
        m = len(image)
        n = len(image[0])
        left = self.findLeft(image, 0, y)
        right = self.findRight(image, y, n-1)
        top = self.findTop(image, 0, x)
        bottom = self.findBottom(image, x, m-1)
        
        return (bottom - top + 1) * (right - left + 1)
    
    
    def isEmptyCol(self, image, y):
        for i in range(len(image)):
            if image[i][y] == '1':
                return False
        return True
        
    def isEmptyRow(self, image, x):
        for i in range(len(image[0])):
            if image[x][i] == '1':
                return False
        return True
        
    def findLeft(self, image, x, y):
        start, end = x, y
        while start + 1 < end:
            mid = int(start + (end - start)/2)
            if self.isEmptyCol(image, mid):
                start = mid
            else:
                end = mid
        
        if not self.isEmptyCol(image, start):
            return start
        return end
        
    def findRight(self, image, x, y):
        start, end = x, y
        while start + 1 < end:
            mid = int(start + (end - start)/2)
            if self.isEmptyCol(image, mid):
                end = mid
            else:
                start = mid
        
        if not self.isEmptyCol(image, end):
            return end
        return start
        
    def findTop(self, image, x, y):
        start, end = x, y
        while start + 1 < end:
            mid = int(start + (end - start)/2)
            if self.isEmptyRow(image, mid):
                start = mid
            else:
                end = mid
        
        if not self.isEmptyRow(image, start):
            return start
        return end
        
    def findBottom(self, image, x, y):
        start, end = x, y
        while start + 1 < end:
            mid = int(start + (end - start)/2)
            if self.isEmptyRow(image, mid):
                end = mid
            else:
                start = mid
        
        if not self.isEmptyRow(image, end):
            return end
        return start
