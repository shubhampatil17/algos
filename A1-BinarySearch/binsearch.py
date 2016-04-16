import unittest
import time

class BinarySearch:        
    def iterative(self, array, left, right, key):
        while left <= right:
            
            mid = left + (right - left)/2
            
            if array[mid] == key:
                return True

            elif array[mid] > key:
                right = mid-1
            
            else:
                left = mid+1
                
            if left > right:
                return False
    
    def recursive(self, array, left, right, key):
        
        if left > right:
            return False
        
        mid = left + (right - left)/2
        
        if array[mid]==key:
            return True
        
        elif array[mid] > key:
            ret = self.recursive(array, left, mid-1, key)
            return ret
        
        else:
            ret = self.recursive(array, mid+1, right, key)
            return ret
            
class Testing(unittest.TestCase):
    def test_iterative(self):
        array = [2,4,6,9,7,10,15,20]  
        #array = [0]*1000
        #array[255]=1
        array = sorted(array) #Write your own sort function here
        startTime = time.time()
        self.assertEqual(BinarySearch().iterative(array, 
                                                  0, 
                                                  len(array)-1, 9), 
                                                  True)
        endTime = time.time()
        
        print "Iterative test completed in (ms):", (endTime - startTime)*1000
        
    def test_recursive(self):
        array = [2,4,6,10,9,7,15,20]
        #array = [0]*1000
        #array[255]=1
        array = sorted(array) #Write your own sort function here
        startTime = time.time()
        self.assertEqual(BinarySearch().recursive(array, 
                                                  0, 
                                                  len(array)-1, 9), 
                                                  True)
        endTime = time.time()
        print "Recursive test completed in (ms):", (endTime - startTime)*1000
                
if __name__ == "__main__":
    unittest.main()
    
#Write a merge or quick sort function instead of using inbuilt function
#to sort array