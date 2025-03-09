import ast

class SymbolTable:
    def extract_symbols(self, code):
        symbols = []
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    symbols.append(("Function", node.name))
                elif isinstance(node, ast.Name):
                    symbols.append(("Variable", node.id))
        except SyntaxError:
            pass
        return symbols
