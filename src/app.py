def is_palindrome(s: str) -> bool:
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    s = s.lower().replace(" ", "")
    return s == s[::-1]
