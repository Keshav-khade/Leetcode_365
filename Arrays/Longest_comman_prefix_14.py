# sorting takes o(n log n) time + o(n) for iteration over minimum string / space complexity o(1)
def long_prefix(strs):
    if len(strs) == 0:
        return ""
    elif len(strs) == 1:
        """lists which has 1 element this is efficient rather than checking for o(n) times"""
        return strs[0]

    strs.sort()

    str1 = strs[0]
    str2 = strs[len(strs)-1]
    n = min(len(str1),len(str2))
    l_prefix = ""

    for i in range(n):
        if str1[i] != str2[i]:
            break
        l_prefix += str1[i]
    return l_prefix

# all the test-case which should worth to remember
# # s = ["",""]
# # s = ["flower","flow","flight"]
# # s = ["dog","racecar","car"]
# # s =["reflower","flow","flight"]
# # s =["reflower","flow","flight"]
# # s = ["a"]
s = ["a"]
res = long_prefix(s)
print(res)

# efficient solution for this problem
def longest(strs):
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""
        return prefix

s = ["a"]
res = longest(s)
print(res)

