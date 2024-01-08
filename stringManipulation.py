# Given a paragraph of text, write a function that:
# 1. Counts the number of words in the paragraph
# 2. Counts the number of characters in the paragraph
# 3. Counts the number of vowels in the paragraph
# 4. Counts the number of consonants in the paragraph
# 5. Counts the number of special characters in the paragraph
# 6. Returns a dictionary with the keys "words", "characters", "vowels", "consonants" and "special characters"

def string_manipulation(paragraph: str) -> dict:
    # return a list with keys name
    return {
        "word": len(paragraph.split()),
        "characters": paragraph.count(' '),
        "vowels": len(list(filter(lambda i: i in 'aeiouAEIOU', paragraph))),
        "consonants": len(list(filter(lambda i: i in 'qwrtypsdfghjklzxcvbnm', paragraph))),
        "special": len(list(filter(lambda i: i in '@!#$%^&^)(}{][', paragraph))),
    }

paragraph = "thE quIck brown fox jump@#$"
print(string_manipulation(paragraph))
