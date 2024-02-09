def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    to_swap = to_swap.lower()
    out = ""

    for ltr in phrase:
    # Check if the lowercase version of the current character matches the lowercase version of to_swap
        if ltr.lower() in to_swap:
            ltr = ltr.swapcase()  # Swap case if it matches
    out += ltr

    return out


# Answer key solution:
#     to_swap = to_swap.lower()
#     out = ""

#     for ltr in phrase:
#         if ltr.lower() == to_swap:
#             ltr = ltr.swapcase()
#         out += ltr

#     return out
