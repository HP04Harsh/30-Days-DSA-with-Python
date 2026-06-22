def reverse(x: int) -> int:
    # 1. Determine the sign
    sign = -1 if x < 0 else 1
    
    # 2. Reverse the absolute number using string slicing
    reversed_str = str(abs(x))[::-1]
    res = sign * int(reversed_str)
    
    # 3. Quick 32-bit overflow check
    if res < -2147483648 or res > 2147483647:
        return 0
        
    return res
