import unicodedata
import json
import hashlib

def remove_accents(input_str):
    """Removes accents and special characters from a string.
    
    This function normalizes the input string and removes accents,
    making comparisons or searches where accents should be ignored easier.

    Examples:
    | ${text_without_accent} = | Remove Accents | Camarão |
    | Should Be Equal As Strings | ${text_without_accent} | Camarao |
    
    | ${result} = | Remove Accents | João |
    | Should Be Equal As Strings | ${result} | Joao |

    Arguments:
    - input_str: (str) The input string containing text with accents.

    Returns:
    - A new string without accents.
    """
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])