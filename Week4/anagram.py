#import anagram_checker

def get_anagrams_from_file(anagram_checker):
        with open(anagram_checker, "r") as f:
            content = f.read()
            return content.split()

def main():
    anagram_checker = anagram_checker.AnagramChecker()
    file_path = "sowpod.txt"  # Replace with the path to your text file
    word_list = get_anagrams_from_file(anagram_checker)
    anagram_checker.check_anagrams(word_list)

    while True:
        user_input = input("Enter a word (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        elif not anagram_checker.is_valid_word(user_input):
            print("Please enter a valid word.")
            continue

        anagrams = anagram_checker.get_anagrams(user_input)
        if anagrams:
            print(f"Anagrams of '{user_input}': {', '.join(anagrams)}")
        else:
            print(f"No anagrams found for '{user_input}'.")
        

        