class TimeMap:

    def __init__(self):
        self.lookup = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.lookup[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.lookup:
            return ""

        if self.lookup[key]:
            res = ""
            myList = self.lookup[key]
            low, high = 0, len(myList) - 1

            while low <= high:
                med = (low + high) // 2
                if myList[med][1] <= timestamp:
                    res = myList[med][0]
                    low = med + 1
                else:
                    high = med - 1
        
        return res
