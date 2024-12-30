from typing import List


# My solution (not working) - I was trying to use a dictionary to store the count of each character
class Solution1:
    def compress(self, chars: List[str]) -> int:
        dict_to_count = dict()
        char_counter = 0
        ind = 0
        for i in range(len(chars)):
            if chars[i] in dict_to_count:
                dict_to_count[chars[i]] += 1
            else:
                dict_to_count[chars[i]] = 1
        array_to_return = []


# My solution 2 (not working) - I was trying to use a counter to store the count of each character
class Solution2:
    def compress(self, chars: List[str]) -> int:
        if len(chars) <= 1:
            return len(chars)

        cur_char = chars[0]
        char_counter_ind = 0
        counter = 1
        i = 1
        while i < len(chars):
            if chars[i] == cur_char and counter <= 1:
                char_counter_ind = i
                counter += 1
                chars[i] = str(counter)
            elif chars[i] == cur_char:
                counter += 1
                chars[char_counter_ind] = str(counter)
                del chars[i]
                i -= 1
            else:
                cur_char = chars[i]
                counter = 1
            i += 1
        return len(chars)


# Optimized solution - use two pointers to read and write the array
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) <= 1:
            return len(chars)

        write_index = 0  # Where to write the next character
        read_index = 0  # Pointer to read through the array

        while read_index < len(chars):
            cur_char = chars[read_index]
            count = 0

            # Count occurrences of the current character
            while read_index < len(chars) and chars[read_index] == cur_char:
                read_index += 1
                count += 1

            # Write the character
            chars[write_index] = cur_char
            write_index += 1

            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1

        return write_index
