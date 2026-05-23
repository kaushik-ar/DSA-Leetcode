import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
                
        def merge(arr, left, mid, right):
            l, r = arr[left:mid+1], arr[mid+1:right+1]
            i, j, k = left, 0, 0
            while j < len(l) and k < len(r):
                if l[j] <= r[k]:
                    arr[i] = l[j]
                    j+=1
                else:
                    arr[i] = r[k]
                    k+=1
                i+=1
            while j < len(l):
                arr[i] = l[j]
                j+=1
                i+=1
            while k < len(r):
                arr[i] = r[k]
                k+=1
                i+=1
                
        def mergeSort(arr, left, right):
            if left == right:
                return arr
            mid = (left+right)//2
            mergeSort(arr, left, mid)
            mergeSort(arr, mid+1, right)
            merge(arr, left, mid, right)
            return arr
        
        return mergeSort(nums, 0, len(nums)-1)
