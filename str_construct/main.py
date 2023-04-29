
class Solution:
    def canConstruct(self, randomNote: str, magazine: str) -> bool:
        if len(randomNote) > len(magazine):
            return False

        str_len = max(len(randomNote), len(magazine))
        randomNote_ch_count = {}
        magazine_ch_count = {}

        for i in range(str_len):
            if i < len(randomNote):
                if None != randomNote_ch_count.get(randomNote[i]):
                    randomNote_ch_count[randomNote[i]] = randomNote_ch_count[randomNote[i]] + 1
                else:
                    randomNote_ch_count[randomNote[i]] = 1

            if i < len(magazine):
                if None != magazine_ch_count.get(magazine[i]):
                    magazine_ch_count[magazine[i]] = magazine_ch_count[magazine[i]] + 1
                else:
                    magazine_ch_count[magazine[i]] = 1

        print(randomNote_ch_count)
        print(magazine_ch_count)

        for key in randomNote_ch_count:
            if None == magazine_ch_count.get(key) or randomNote_ch_count[key] > magazine_ch_count[key]:
                return False

        return True

# class Solution2:
#     def canConstruct(self, randomNote: str, magazine: str) -> bool:
#         if len(randomNote) > len(magazine):
#             return False
#
#         str_len = max(len(randomNote), len(magazine))
#         randomNote_ch_count = [0]*26
#         magazine_ch_count = [0]*26
#         for i in range(str_len):
#             if i < len(randomNote):
#                 order = ord(randomNote[i]) - ord('a')
#                 randomNote_ch_count[order] = randomNote_ch_count[order] + 1
#
#             if i < len(magazine):
#                 order = ord(magazine[i]) - ord('a')
#                 magazine_ch_count[order] = magazine_ch_count[order] + 1
#
#         #print(randomNote_ch_count)
#         #print(magazine_ch_count)
#
#         for i in range(26):
#             if randomNote_ch_count[i] > magazine_ch_count[i]:
#                 return False
#
#         return True
#
#
# class Solution1:
#     def canConstruct(self, randomNote: str, magazine: str) -> bool:
#         randomNote_len = len(randomNote)
#         magazinelist = list(magazine)
#         magazine_len = len(magazinelist)
#
#         print(magazinelist)
#
#         for i in range(randomNote_len):
#             for j in range(magazine_len):
#                 if randomNote[i]==magazinelist[j]:
#                     del magazinelist[j]
#                     break
#             if j==magazine_len:
#                 return False
#
#         return True
#
#
# import time
#
# if __name__ == '__main__':
#     solution=Solution()
#     randomNote = 'aadevfvccsdgsss'
#     magazine = 'aabcddevvssffcccgss'
#     start=time.perf_counter()
#     result = solution.canConstruct(randomNote, magazine)
#     end=time.perf_counter()
#     print('excute time', end-start)
#     print(result)
