import math


class PaginationHelper:
    def __init__(self, items, num):
        self.items = items
        self.amountPerPage = num
        self.amountOfItems = len(self.items)

    def pageCount(self):
        return math.ceil(self.amountOfItems / self.amountPerPage)

    def itemCount(self):
        return self.amountOfItems

    def pageItemCount(self, page):
        if page < 0 or page > self.pageCount() - 1:
            return -1
        if page == self.pageCount() - 1:
            if self.amountOfItems % self.amountPerPage != 0:
                return self.amountOfItems % self.amountPerPage
        return self.amountPerPage

    def pageIndex(self, index):
        if index < 0 or index >= self.amountOfItems:
            return -1
        return math.floor(index / self.amountPerPage)


# x = PaginationHelper(["a", "b", "c", "d", "e", "f"], 4)
# x = PaginationHelper([], 2)
# x = PaginationHelper(["a", "b", "c", "d", "e", "f","g","h"], 4)
x = PaginationHelper(["a", "b", "c", "d", "e", "f","a", "b", "c", "d", "e", "f","g","h"], 13)
x = PaginationHelper(["a", "b", "c", "d", "e", "f","a", "b", "c", "d", "e", "f","g","h"], 18)
x = PaginationHelper(["a", "b", "c", "d", "e", "f","a", "b", "c", "d", "e", "f","g","h"], 5)

print(x.pageCount())
print(x.itemCount())
print(x.pageItemCount(0))
print(x.pageItemCount(1))
print(x.pageItemCount(2))
print(x.pageIndex(5))
print(x.pageIndex(2))
print(x.pageIndex(20))
print(x.pageIndex(-10))
