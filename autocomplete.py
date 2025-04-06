# autocomplete.py

from compiler.lexer import lexer
import json

class AutoCompleteEngine:
    def __init__(self, symbol_table_path="compiler/symbol_table.json"):
        self.symbols = self.load_symbols(symbol_table_path)
        self.builtin_suggestions = ['print', 'input', 'if', 'else', 'for', 'while', 'def', 'return']

    def load_symbols(self, path):
        try:
            with open(path, "r") as f:
                return json.load(f).get("symbols", [])
        except FileNotFoundError:
            return []

    def suggest(self, code_fragment):
        suggestions = []

        # Match against symbol table entries
        for entry in self.symbols:
            name = entry.get("name", "")
            symbol_type = entry.get("type", "")
            if name.startswith(code_fragment):
                suggestions.append(f"{name} ({symbol_type})" if symbol_type else name)

        # Match against built-in keywords
        for kw in self.builtin_suggestions:
            if kw.startswith(code_fragment):
                suggestions.append(kw)

        return list(set(suggestions))  # remove duplicates

# Example usage
if __name__ == "__main__":
    # Tokenize to simulate compiler's start (not necessary but nice for context)
    input_code = "x = 5 + 10"
    lexer.input(input_code)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

    # Autocomplete interaction
    engine = AutoCompleteEngine()
    user_input = input("Start typing code: ")
    suggestions = engine.suggest(user_input)
    print("Suggestions:", suggestions)
