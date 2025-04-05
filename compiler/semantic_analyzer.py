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
