class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.set = set()
        self.index = 0

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = index
            self.set.add(val)
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            
            del self.hashmap[val]
            self.set.remove(val)
            return True

        return False

    def getRandom(self) -> int:
        randomIndex = random.randint(0,len(self.hashmap)-1)
        lst = list(self.set)
        return lst[randomIndex]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()