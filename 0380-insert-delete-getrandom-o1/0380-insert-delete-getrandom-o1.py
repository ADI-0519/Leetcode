import random
class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(self.arr)
            self.arr.append(val)
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            index = self.hashmap[val]
            self.hashmap[self.arr[-1]] = index
            self.arr[index],self.arr[-1] = self.arr[-1],self.arr[index]
            self.arr.pop()
            del self.hashmap[val]
            return True

        return False

    def getRandom(self) -> int:
        randomIndex = random.randint(0,len(self.arr)-1)
        return self.arr[randomIndex]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()