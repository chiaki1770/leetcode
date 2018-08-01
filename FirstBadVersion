def findFirstBadVersion(self, n):
    start, end = 1, n
    while start + 1 < end:
        mid = int(start + (end - start) / 2)
        if SVNRepo.isBadVersion(mid):
            end = mid
        else:
            start = mid

    if SVNRepo.isBadVersion(start):
        return start

    return end
