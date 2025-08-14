def can_form_palindrome(s):
    flag = 0
    for ch in s:
        pos = ord(ch) - ord('a')  # finding the current position of the character i.e. ip- bad,    b-a = 2-1 = 1  so, 1 0 , then 1 1
        flag = flag ^ (1 << pos)        # toggle the bit

    # Check: 0 for even palindrome, power of 2 for odd palindrome
    if flag == 0 or (flag & (flag - 1)) == 0:
        return True
    else:
        return False

# Examples
print(can_form_palindrome("civic"))   # True (odd palindrome)
