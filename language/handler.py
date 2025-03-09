# TRANSCRIBE

import re
import json
import os
import sys

def extract_words_from_markdown(md_file):
    """Extracts a set of unique words from a markdown file."""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File {md_file} not found.")
        sys.exit(1)
        
    # Use a regex to extract words (letters, numbers, underscores)
    words = re.findall(r'\b\w+\b', content)
    # Convert to lowercase and get unique words
    return set(word.lower() for word in words)

def load_correct_words(json_file):
    """Loads the set of already-confirmed correct words from a JSON file."""
    if os.path.exists(json_file):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            # Assuming the JSON file contains a list of words
            return set(data)
        except json.JSONDecodeError:
            print("Error decoding JSON. Starting with an empty list.")
            return set()
    else:
        return set()

def save_correct_words(json_file, words):
    """Saves the set of correct words to a JSON file as a sorted list."""
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(sorted(list(words)), f, indent=4)

def main():
    markdown_file = input("MD: ")
    json_file = input("JSON: ")
    
    # Extract words from the markdown file
    markdown_words = extract_words_from_markdown(markdown_file)
    # Load the already-confirmed correct words
    known_correct_words = load_correct_words(json_file)
    
    # Identify new words that haven't been confirmed yet
    new_words = markdown_words - known_correct_words
    
    # Ask the user about each new word
    for word in sorted(new_words):
        answer = input(f"Is the word '{word}' spelled correctly? (y/n or m to first uppercase): ")
        if answer.strip().lower() == 'y':
            known_correct_words.add(word)
        elif answer.strip().lower() == "m":
            known_correct_words.add(word.capitalize())
    
    # Save the updated set to the JSON file
    save_correct_words(json_file, known_correct_words)
    print("Correct words have been saved to", json_file)

if __name__ == '__main__':
    main()
