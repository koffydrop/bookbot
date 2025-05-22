import sys
import stats

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def main():
    text = get_book_text(book_path)
    word_count = stats.get_word_count(text)
    char_counts = stats.get_character_count(text)
    sorted = stats.sort_fmt_char_count(char_counts)
    filtered = []
    for char_dict in sorted:
        if char_dict["char"].isalpha():
            filtered.append(char_dict)

    formatted_char_count = []
    for it in filtered:
        formatted_char_count.append(f"{it['char']}: {it['num']}")

    output = f"""
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{"\n".join(formatted_char_count)}
============= END ===============
"""
    print(output)


main()
