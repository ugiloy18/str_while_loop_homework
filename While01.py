def main(s):
    """"
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count = 0
    i = 0
    while i < len(s):
        if s[i].isdigit():
            count += 1
        i += 1
    return count 
print(main("bab5vt4b9"))
print(main("kur85n48f85hr4r8hf84"))