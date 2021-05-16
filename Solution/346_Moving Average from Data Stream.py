class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.vals = []

    def next(self, val: int) -> float:
        size, vals = self.size, self.vals
        vals.append(val)
        window_sum = sum(vals[-size:])
        return window_sum / min(len(vals), size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
if __name__ == '__main__':
    # ["MovingAverage", "next", "next", "next", "next"]
    # [[3], [1], [10], [3], [5]]
    obj = MovingAverage(3)
    param1 = obj.next(1)
    param2 = obj.next(10)
    param3 = obj.next(3)
    param4 = obj.next(5)
    print(param4)

