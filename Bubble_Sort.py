def bubble_sort(nums):
    n = len(nums)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


num_input = input("Enter numbers separated by commas: ")
nums = [int(num) for num in num_input.split(",")]

# Call bubble sort function and print the sorted list
sorted_nums = bubble_sort(nums)
print("Sorted list:", sorted_nums)
