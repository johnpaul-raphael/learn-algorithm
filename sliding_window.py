# static/fixed sliding window
def static_fixed_sliding_window(arr, window_size):
    # edge case scenario
    if len(arr) < window_size <= 0:
        return []

    result = []

    # calculate initial window_size
    window_sum = sum(arr[:window_size])
    result.append(window_sum)

    for index in range(len(arr) - window_size):
        right_index = index + window_size
        window_sum = window_sum - arr[index] + arr[right_index]
        result.append(window_sum)

    return result


input_value = [1, 3, 5, 6, 7, 8, 9]
size = 3
response = static_fixed_sliding_window(input_value, size)
print(response)
print(f'minimum array sum {min(response)}')
print(f'maximum array sum {max(response)}')


def dynamic_sliding_window(dynamic_input_value, target_value):
    window_start_index = 0
    window_sum = 0
    min_len = float('inf')

    for window_end_index in range(len(dynamic_input_value)):
        window_sum += dynamic_input_value[window_end_index]

        while window_sum >= target_value:
            min_len = min(min_len, window_end_index - window_start_index + 1)
            window_sum -= dynamic_input_value[window_start_index]
            window_start_index += 1

    return min_len if min_len != float('inf') else 0


dynamic_input_arr = [2, 3, 1, 2, 4, 3]
dynamic_result = dynamic_sliding_window(dynamic_input_arr, 7)
print(f'dynamic sliding window result: {dynamic_result}')
