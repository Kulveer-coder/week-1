

# add code below ...
def palindrome (word):
    """check whether a word or phrase is a palindrome."""
    clean_word = ""
    for character in word.lower():
        if character.isalnum():
            clean_word += character
    return clean_word == clean_word[::-1]


def parentheses(sequence):
    stack = []
    for char in sequence:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0
