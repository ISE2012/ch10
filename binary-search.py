# Returns index of x in arr if present, else -1 
def binary_search(arr, low, high, x): 
  
    # Check base case 
    if high >= low: 
  
        mid = (high + low) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        # Element is not present in the array 
        return -1
  
    
def main():
    # Test array 
    arr = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 
    find_X = "MAD"
  
    # Function call 
    result = binary_search(arr, 0, len(arr)-1, find_X) 
    print("Array:",arr)
    print("Find:", find_X)
    if result != -1: 
        print("Element is present at index", str(result)) 
    else: 
        print("Element is not present in array") 

# run main()
main()

