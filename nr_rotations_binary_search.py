def count_rotations_binary(nums):
    lo = 0
    hi = len(nums)
    if len(nums) == 0:
        return 0
    while lo<=hi:
        mid = (lo+hi)//2
        mid_number = nums[mid]
        
        # Uncomment the next line for logging the values and fixing errors.
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid > 0 and mid_number > nums[mid-1] and mid_number > nums[mid+1]:
            # The middle position is the answer
            return mid+1
        
        elif mid_number < nums[mid+1] and mid_number > nums[mid-1]:
            # Answer lies in the left half
            hi = mid - 1

        elif mid == 0:
            if mid_number == nums[mid] and mid_number > mid_number[mid+1]:
                return mid+1
            elif mid_number == nums[mid] and mid_number < mid_number[mid+1]:
                return mid
            elif mid_number == nums[mid] and len(nums) == 0:
                return 0
        
        else:
            # Answer lies in the right half
            lo = mid + 1
    
    return -1


print(count_rotations_binary([1]))