#User function Template for python3

class Solution: 
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1):
            min_index = i
            for j in range(min_index+1,n):
                if arr[j] < arr[min_index]:
                    min_index = j
            if i != min_index:
                arr[i] , arr[min_index] = arr[min_index] , arr[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
