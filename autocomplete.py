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

    def suggest(self, code_fragment):  # ← Now it's a method of the class
        suggestions = []
        builtin_suggestions = ['print', 'input', 'if', 'else', 'for', 'while', 'def', 'return']

        for entry in self.symbols.get('symbols', []):
            name = entry.get('name')
            if name and name.startswith(code_fragment):
                suggestions.append(name)

        suggestions.extend([kw for kw in builtin_suggestions if kw.startswith(code_fragment)])
        return list(set(suggestions))
    
if __name__ == "__main__":
    engine = AutoCompleteEngine()
    user_input = input("Start typing code: ")
    suggestions = engine.suggest(user_input)
    print("Suggestions:", suggestions)


