def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    backwards = list(phrase)
    backwards.reverse()
    return ''.join(backwards)

