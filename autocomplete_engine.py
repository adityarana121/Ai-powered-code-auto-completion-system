
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
import re

# Example keywords and functions to suggest
SUGGESTIONS = ["print", "input", "int", "float", "for", "while", "if", "else", "def", "return"]

class CodeAutoCompleter(Completer):
    def get_completions(self, document, complete_event):
        word = document.get_word_before_cursor()
        for suggestion in SUGGESTIONS:
            if suggestion.startswith(word):
                yield Completion(suggestion, start_position=-len(word))

def main():
    completer = CodeAutoCompleter()
    while True:
        user_input = prompt(">>> ", completer=completer, complete_while_typing=True)
        print("You typed:", user_input)

if __name__ == "__main__":
    main()
