import ast

class Parser:
    def parse(self, code):
        try:
            tree = ast.parse(code)
            parse_table = self.generate_parse_table(tree)
            return ast.dump(tree, indent=2), parse_table
        except SyntaxError as e:
            return str(e), {}

    def generate_parse_table(self, tree):
        table = {}
        for node in ast.walk(tree):
            node_type = type(node).__name__
            if node_type not in table:
                table[node_type] = 0
            table[node_type] += 1
        return table
