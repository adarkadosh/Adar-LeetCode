class Solution1:
    def isHappy(self, n: int) -> bool:
        table = set()
        cur_list = [int(char) for char in str(n)]
        cur_sum = 0
        while cur_sum != 1:
            if cur_sum in table:
                return False

            table.add(cur_sum)
            cur_sum = 0

            for i in range(len(cur_list)):
                cur_sum += cur_list[i] * cur_list[i]
            cur_list = [int(char) for char in str(cur_sum)]
            print(cur_list, cur_sum)
        return True


# Optimized solution - use Floyd's cycle detection algorithm
class Solution2:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1


# Optimized solution - by chat
class Solution:
    def isHappy(self, n: int) -> bool:
        table = set()  # Use a set to track sums for better performance
        cur_sum = n

        while cur_sum != 1:
            if cur_sum in table:  # Detect cycles
                return False
            table.add(cur_sum)  # Mark this sum as seen

            # Calculate the next sum of squares of digits
            cur_sum = sum(int(char) ** 2 for char in str(cur_sum))

        return True
