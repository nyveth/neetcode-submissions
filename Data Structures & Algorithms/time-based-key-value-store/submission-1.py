class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.data:
            self.data[key] = []

        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        cur_data = self.data[key]
        l = 0
        r = len(cur_data) - 1

        while r >= l:
            mid = (r + l) // 2
            if timestamp >= cur_data[mid][0]:
                l = mid + 1
            else:
                r = mid - 1
            
        return "" if r == -1 else cur_data[r][1]
        
