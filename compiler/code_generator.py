class CodeGenerator:
    def generate(self, node):
        if node.type == 'stmt':
            # Assume it's a wrapper, so just generate code for its child
            return self.generate(node.children[0])

        elif node.type == 'assign':
            var_name = node.children[0].value
            expr_code = self.generate(node.children[1])
            return f"{var_name} = {expr_code}"

        elif node.type == 'binop':
            left = self.generate(node.children[0])
            right = self.generate(node.children[1])
            return f"({left} {node.value} {right})"

        elif node.type == 'num':
            return str(node.value)

        elif node.type == 'var':
            return node.value

        else:
            raise Exception(f"Unknown node type: {node.type}")
