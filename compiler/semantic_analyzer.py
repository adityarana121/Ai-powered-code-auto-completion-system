import json

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def analyze(self, node):
        print(f"[DEBUG] Type of node received in analyzer: {type(node)}")
        if node.type == 'assign':
            var_name = node.children[0].value
            self.symbol_table[var_name] = 'int'
        elif node.type == 'var':
            var_name = node.value
            if var_name not in self.symbol_table:
                raise Exception(f"Undefined variable: {var_name}")

    def print_table(self):
        print("\n🧠 Symbol Table:")
        for var, typ in self.symbol_table.items():
            print(f"  {var} : {typ}")

    def export_table(self, filepath="symbol_table.json"):
        with open(filepath, "w") as f:
            json.dump(self.symbol_table, f, indent=4)
        print(f"\n✅ Symbol table exported to '{filepath}'")
