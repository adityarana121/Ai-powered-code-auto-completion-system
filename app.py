from flask import Flask, render_template, request, jsonify
from modules.lexer import Lexer
from modules.parser import Parser
from modules.symbol_table import SymbolTable
from modules.autocomplete import Trie
from modules.ml_suggester import ml_suggest

app = Flask(__name__)

# Initialize modules
lexer = Lexer()
parser = Parser()
symbol_table = SymbolTable()
trie = Trie()

# Preload common keywords for suggestions
keywords = [
    "for", "while", "def", "class", "print", "return", "if", "else", "import", "from",
    "try", "except", "finally", "with", "as", "lambda", "yield", "async", "await",
    "map", "filter", "reduce", "len", "open", "range", "list", "dict", "set", "tuple"
]
for word in keywords:
    trie.insert(word)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process_code", methods=["POST"])
def process_code():
    data = request.get_json()
    code_snippet = data.get("code", "").strip()

    if not code_snippet:
        return jsonify({"error": "No code provided!"})

    try:
        # Perform lexical analysis
        tokens = lexer.tokenize(code_snippet)

        # Parse code and generate AST & parse table
        ast_tree, parse_table = parser.parse(code_snippet)

        # Extract symbols
        symbols = symbol_table.extract_symbols(code_snippet)

        # Generate Trie-based code suggestions
        last_word = code_snippet.split()[-1] if code_snippet.split() else ""
        trie_suggestions = trie.suggest(last_word) if last_word else []

        # Generate ML-based code suggestions
        ml_suggestions = ml_suggest(code_snippet) if code_snippet else ""

        return jsonify({
            "tokens": tokens,
            "ast": ast_tree,
            "parse_table": parse_table,
            "symbol_table": symbols,
            "trie_suggestions": trie_suggestions if trie_suggestions else ["No suggestions"],
            "ml_suggestions": ml_suggestions if ml_suggestions else "No AI suggestions"
        })
    except Exception as e:
        return jsonify({"error": f"Processing failed: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
