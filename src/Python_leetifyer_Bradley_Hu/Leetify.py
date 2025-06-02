# Leetify.py
# This script converts a given text into "leet" speak(a.k.a Hacker Speak), where letters are replaced with similar-looking symbols or numbers.
def leetify(text: str) -> str:
    """Leetify a given text by replacing letters with leet speak equivalents.
    This function takes a string input and replaces each letter with its corresponding leet speak character.

    Args:
        text (str): The text to be converted to leet speak.

    Returns:
        str: The leetified version of the input text.
    """
    leet_dict = {
        'a': '@', 'A': '@',
        'b': '|3', 'B': '|3',
        'c': '<', 'C': '<',
        'd': '|)', 'D': '|)',
        'e': '[-', 'E': '[-',
        'f': '|=', 'F': '|=',
        'g': '&', 'G': '&',
        'h': '|-|', 'H': '|-|',
        'i': '|', 'I': '|',
        'j': ',_|', 'J': ',_|',
        'k': '|<', 'K': '|<',
        'l': '|_', 'L': '|_',
        'm': '|\\/|', 'M': '|\\/|',
        'n': '|\\|', 'N': '|\\|',
        'o': '()', 'O': '()',
        'p': '|*', 'P': '|*',
        'q': '(_,)', 'Q': '(_,)',
        'r': '.-', 'R': '.-',
        's': '$', 'S': '$',
        't': "'|'", 'T': "'|'",
        'u': '|_|', 'U': '|_|',
        'v': '\\/', 'V': '\\/',
        'w': '\\/\\/', 'W': '\\/\\/',
        'x': '><', 'X': '><',
        'y': '`/', 'Y': '`/',
        'z': '-/_', 'Z': '-/_'
    }
    return ''.join(leet_dict.get(c, c) for c in text)
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python Leetify.py <text>")
        sys.exit(1)
    
    input_text = " ".join(sys.argv[1:])
    leet_text = leetify(input_text)
    print(leet_text)