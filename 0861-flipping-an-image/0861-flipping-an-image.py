class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for arr in image:
            arr.reverse()
            for i,element in enumerate(arr):
                arr[i] = int(not(element))

        return image
