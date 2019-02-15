class Sol:
    def insert_pos(self,arr, l, r, x):
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return l
p1=Sol()
r = p1.insert_pos([2, 3, 4, 10, 40], 0, 4, 15)
print(r)
