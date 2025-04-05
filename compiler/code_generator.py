
class CodeGenerator:
    def __init__(self):
        self.temp_count = 0
        self.code = []

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def generate(self, node):
        if node['type'] == 'assign':
            target = node['children'][0]['value']
            expr = self.generate(node['children'][1])
            self.code.append(f"{target} = {expr}")
            return target
        elif node['type'] == 'binop':
            left = self.generate(node['children'][0])
            right = self.generate(node['children'][1])
            temp = self.new_temp()
            self.code.append(f"{temp} = {left} {node['value']} {right}")
            return temp
        elif node['type'] == 'num':
            return str(node['value'])
        elif node['type'] == 'var':
            return node['value']
