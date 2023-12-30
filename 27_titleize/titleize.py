def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """


    lst = phrase.lower().split(" ")
    for idx in range(len(lst)):
        lst[idx] = lst[idx].capitalize()
    return " ".join(lst)