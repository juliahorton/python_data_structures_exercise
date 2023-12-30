def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    if parens[0] == ")" or parens[-1] == "(":
        return False
    if len(parens) % 2 != 0:
        return False
    if parens.count("(") != parens.count(")"):
        return False 
    return True