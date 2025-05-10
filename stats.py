def get_word_count(text: str) -> int:
    return len(text.split())

def get_character_count(text: str) -> dict:
    totals = {}
    for char in text:
        char = char.lower()
        if char not in totals:
            totals[char] = 1
        else:
            totals[char] += 1
    return totals

def sort_fmt_char_count(input: dict) -> list[dict]:
    list = []
    for char in input:
        list.append({ "char": char, "num": input[char]})
    list.sort(key = lambda d: d["num"], reverse = True)
    return list
