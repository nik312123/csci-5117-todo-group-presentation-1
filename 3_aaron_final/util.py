def snake_case_to_camel_case(string: str) -> str:
    """
    Returns the camel case version of a given snake case string.
    :param string: The snake case string to convert to camel case
    :return: The camel case version of a given snake case string
    """
    word_parts = string.split("_")
    return word_parts[0] + "".join(word.capitalize() for word in string.split("_")[1:])
