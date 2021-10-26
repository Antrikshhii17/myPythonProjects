""" Longest substring with unique characters. Returns length of longest unique substring.
From Leetcode """


def longeststring(string) -> int:
    begin = end = ans = 0
    seen = set()
    while begin < len(string) and end < len(string):
        if string[end] not in seen:
            seen.add(string[end])
            end += 1
            ans = max(ans, end - begin)
        else:
            seen.remove(string[begin])
            begin += 1
    return ans


if __name__ == "__main__":
    string = 'ababaabbbbbbbbaaaarhytmbaaaabbabababbaabbabababab'
    result = longeststring(string)
    print(result)
