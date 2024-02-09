def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
# built in:
    return phrase.capitalize()

# manual:
    return phrase[:1].upper() + phrase[1:]