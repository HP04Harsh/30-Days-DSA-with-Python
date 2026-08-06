def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""
    strs.sort()  # Sort karne par pehla aur aakhri word sabse alag honge
    first, last = strs[0], strs[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    return first[:i]