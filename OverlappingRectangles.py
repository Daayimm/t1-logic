class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def doOverlap(l1,r1,l2,r2):
    
    if(r1.x < l2.x or l1.x > r2.x or r1.y>l2.y or l1.y < r2.y ):
        return False
    else:
        return True
    
if __name__ == "__main__":
    l1 = Point(0, 10)
    r1 = Point(10, 0)
    l2 = Point(5, 5)
    r2 = Point(15, 0)

    if doOverlap(l1, r1, l2, r2):
        print("Test 1: Rectangles Overlap")
    else:
        print("Test 1: Rectangles Don't Overlap")

    # No overlap - rect2 is to the right
    l1 = Point(0, 10)
    r1 = Point(5, 0)
    l2 = Point(6, 10)
    r2 = Point(10, 0)
    if doOverlap(l1, r1, l2, r2):
        print("Test 2: Rectangles Overlap")
    else:
        print("Test 2: Rectangles Don't Overlap")

    # No overlap - rect2 is above
    l1 = Point(0, 4)
    r1 = Point(4, 0)
    l2 = Point(0, 10)
    r2 = Point(4, 5)
    if doOverlap(l1, r1, l2, r2):
        print("Test 3: Rectangles Overlap")
    else:
        print("Test 3: Rectangles Don't Overlap")
