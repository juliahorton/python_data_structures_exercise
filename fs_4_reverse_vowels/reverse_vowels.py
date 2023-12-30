def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    lst = list(s)
    new_lst = []
    for idx in range(len(lst)):
        if lst[idx] in "aeiouAEIOU":
            new_lst.append(lst[idx])
            lst[idx] = ""
    new_lst = new_lst[::-1]
    for idx in range(len(lst)):
        if lst[idx] == "":
            lst[idx] = new_lst.pop(0)
    return "".join(lst)