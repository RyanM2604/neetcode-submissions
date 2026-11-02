class TimeMap:

    def __init__(self):
        self.lookup = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.lookup[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.lookup[key]
        low, high = 0, len(arr) - 1
        res = ""

        while low <= high:
            mid = (low + high) // 2

            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                low = mid + 1
            else:
                high = mid - 1
        
        return res