'''
Sliding window is best for questions on subarrays or substrings. 
Instead of recalculating data repeatedly, we maintain a "window" that moves through the array or string.

Fixed Window Example: Find the maximum sum of any subarray of size k.
Dynamic Window: The size of the window can expand or shrink.
Example: Find the smallest subarray with a sum >= target.
'''
def fixed_sliding_window(arr, k):
    # Initialize variables
    max_result = float('-inf')  # Or 0, depending on the problem
    current_window_sum = 0

    # Traverse through the array
    for right in range(len(arr)):
        # Add the current element to the window
        current_window_sum += arr[right]

        # When the window reaches size k
        if right >= k - 1:
            # Update the result based on the problem
            max_result = max(max_result, current_window_sum)  # Example: find max sum

            # Shrink the window by removing the element at the left
            current_window_sum -= arr[right - (k - 1)]

    return max_result



def sliding_window(arr, target):
    left = 0
    current_sum = 0  
    result = float('inf')  

    for right in range(len(arr)):
        # Add current element to the window
        current_sum += arr[right]

        # Shrink the window until the condition is satisfied
        while current_sum >= target:
            result = min(result, right - left + 1) 
            current_sum -= arr[left]
            left += 1

    return result if result != float('inf') else -1

