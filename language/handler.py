# IMPORT COMMON MODULES
import re
import json
import os
import sys

# WORD EXTRACTOR
def extract_words_from_markdown(md_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    words = re.findall(r'\b\w+\b', content)
    return set(word.lower() for word in words)

# LOADS JSON
def load_correct_words(json_file):
    if os.path.exists(json_file):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return set(data)
        except json.JSONDecodeError:
            print("Error decoding JSON. Starting with an empty list.")
            return set()
    else:
        return set()

# SAVES FILE
def save_correct_words(json_file, words):
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(sorted(list(words)), f, indent=4)

# MAIN FUNCTION
def main():
    # FILE INPUT
    markdown_file = input("MD: ")
    json_file = input("JSON: ")
    # EXTRACT WORDS
    markdown_words = extract_words_from_markdown(markdown_file)
    known_correct_words = load_correct_words(json_file)
    # IDENTIFY NEW WORDS
    new_words = markdown_words - known_correct_words
    # ASK USER ABOUT EACH WORD
    for word in sorted(new_words):
        answer = input(f"Is the word '{word}' spelled correctly? (y/n or m to first uppercase): ")
        if answer.strip().lower() == 'y':
            known_correct_words.add(word)
        elif answer.strip().lower() == "m":
            known_correct_words.add(word.capitalize())
    # SAVE
    save_correct_words(json_file, known_correct_words)
    print("Correct words have been saved to", json_file)

if __name__ == '__main__':
    main()
