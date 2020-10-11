from random import randrange

def generate_id(length):
    result = ""
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    characters_length = len(characters)
    for x in range(length):
        result += characters[randrange(characters_length)]
    return result