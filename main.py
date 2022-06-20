import math


def smallest_subarray_sum(s, arr):
    # TODO: Write your code here

    min_length = math.inf;
    #curr_len = 0;

    sum = 0;

    window_start = 0;
    #window_end = 0;
    #idx_tracker = 0

    # Add all elements until we get to greater than or equal to 'S'

    for element_idx in range(len(arr)):
        #print("element_idx", element_idx)
        sum += arr[element_idx]

        while sum >= s:
            window_end = element_idx

            window_length = window_end - window_start + 1

            min_length = min(min_length, window_length)

            sum -= arr[window_start]

            window_start += 1

            min_length = min(min_length, window_length)



    print("min_length", min_length)
    return -1

smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2]);
smallest_subarray_sum(7, [2, 1, 5, 2, 8]);
smallest_subarray_sum(8, [3, 4, 1, 1, 6]);
