class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol ={'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1, 'S': 0}
        pre_value = 10000
        cur_value = 0
        value = 0
        s = s + "S"
        for i in s:
            cur_value = symbol[i]
            if cur_value < pre_value:
                value += pre_value
                pre_value = cur_value
            elif cur_value == pre_value:
                pre_value += cur_value
            else:
                pre_value = cur_value - pre_value

        return value - 10000
