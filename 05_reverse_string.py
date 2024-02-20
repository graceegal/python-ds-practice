def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
# TODO: reverse using [::-1]
    backwards = list(phrase)
    backwards.reverse()
    return ''.join(backwards)

