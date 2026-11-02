class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        arr = self.map[key]
        low = 0
        high = len(arr) - 1
        res = ""

        # We need the highest timestamp value that is still <= timestamp of "get"

        while low <= high:
            mid = (low + high) // 2

            if arr[mid][0] <= timestamp: # Passes monotonic condition:
                res = arr[mid][1]
                low = mid + 1
            else:
                high = mid - 1
        
        return res


# [(1, happy), (3, sad)]



