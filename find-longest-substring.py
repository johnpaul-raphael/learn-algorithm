def longestSubstring(input_value: str) -> int:
    start = 0
    sub_arr_dic = {}
    max_sub_str_len = 0

    # looping all the value to check possible longest substring
    for end in range(len(input_value)):
        current_value = input_value[end]

        if current_value in sub_arr_dic and sub_arr_dic[current_value] >= start:
            start = sub_arr_dic[current_value] + 1

        sub_arr_dic[current_value] = end
        print(sub_arr_dic)

        max_sub_str_len = max(max_sub_str_len, end - start + 1)

    return max_sub_str_len


str_input = 'abbcanbcbb'
print(f'longest substring is {longestSubstring(str_input)}')
