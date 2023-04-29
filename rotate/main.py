# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        move_cnt = 0
        start = 0
        length = len(nums)
        pos = 0
        next = 0
        tmp1 = 0
        tmp2 = 0
        #print(nums)
        while start < length:
            pos = start
            tmp1 = nums[pos]
            while 1:
                next = (pos+k)%length
                tmp2 = nums[next]
                nums[next] = tmp1
                tmp1 = tmp2
                move_cnt += 1
                pos = next
                if pos == start or move_cnt == length:
                    break
                #print(pos)
                #print(tmp1)
                #print(nums)
            start += 1
            if move_cnt == length:
                break



# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     solution = Solution()
#     num_test = [23, 23, 222, 1, 232323, 12313, 1251411, 123123]
#     k = 3
#     solution.rotate(num_test, 4)
#     print(num_test)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


