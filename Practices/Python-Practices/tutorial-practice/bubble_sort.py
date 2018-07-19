"""Bubble sort function
The function should take one inputs:
The input_array which want to be sort. 
A sorted(ascending order) array will be returned for this function.
For those arraies who have length of 0 or 1, return the input array
itself."""
import unittest
def bubble_sort(input_array, order='DESC'):
    """
    Swap repeatedly the adjacent elements if they are in wrong order.
    """
    #Create a copy of input_array to fulfill out of place sorting
    input_array=input_array[:]
    n=len(input_array)
    if not input_array or n==1: 
        return input_array
    for i in range(n-1):
        for j in range(n-1-i):
            if order=='DESC':
                if input_array[j]<input_array[j+1]:
                    input_array[j],input_array[j+1]=input_array[j+1],input_array[j]
            if order=='ASCE':
                if input_array[j]>input_array[j+1]:
                    input_array[j],input_array[j+1]=input_array[j+1],input_array[j]
    return input_array 

def check_result(array, order):
    """
    check an array whether is in a descending or ascending order
    input: array, order 
    output: True/ False 
    """
    if order=='ASCE':
        for i in range(len(array)-1):
            if array[i]>array[i+1]:
                return False
    if order=='DESC':
        for i in range(len(array)-1):
            if array[i]<array[i+1]:
                return False
    #For array whose length =1, return True
    return True

class MyTest(unittest.TestCase):
    def groud_truth(self):    
        groud_truth_asc=[1,2,3]
        self.assertEqual(check_result(groud_truth_asc, 'ASCE'), True)
        groud_truth_des=[3,2,1]
        self.assertEqual(check_result(groud_truth_des, 'DESC'), True)

    def test_case(self):
        #Staring with the length of input array of 1
        input_array=[1]
        result_asc=(bubble_sort(input_array, 'ASCE')) 
        result_des=(bubble_sort(input_array, 'DESC'))
        #Both should return true
        self.assertTrue(check_result(result_asc,'ASCE'))
        self.assertTrue(check_result(result_des,'DESC'))
        
        #Test case with unordered array (length!=1)
        input_array= [1,3,9,15,4,19,29]
        result_asc=(bubble_sort(input_array, 'ASCE')) 
        result_des=(bubble_sort(input_array, 'DESC'))
        #Both should return true
        self.assertTrue(check_result(result_asc,'ASCE'))
        self.assertTrue(check_result(result_des,'DESC'))

if __name__ == '__main__':
    unittest.main()
    
                    