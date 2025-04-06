# autocomplete.py
from compiler.lexer import lexer
import json

class AutoCompleteEngine:
    def __init__(self, symbol_table_path="compiler/symbol_table.json"):
        self.symbols = self.load_symbols(symbol_table_path)

    def load_symbols(self, path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def suggest(self, input_code):
        lexer.input(input_code)
        tokens = [tok.value for tok in lexer]
        if not tokens:
            return []

        last_token = tokens[-1]
        suggestions = []

        for symbol in self.symbols:
            if symbol.startswith(last_token):
                suggestions.append(symbol)

        return suggestions

# Example usage
if __name__ == "__main__":
    engine = AutoCompleteEngine()
    user_input = input("Start typing code: ")
    suggestions = engine.suggest(user_input)
    print("Suggestions:", suggestions)

