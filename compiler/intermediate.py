class ASTNode:
    def __init__(self, node_type, value=None, children=None):
        self.node_type = node_type
        self.value = value
        self.children = children if children else []

    def to_dict(self):
        return {
            'type': self.node_type,
            'value': self.value,
            'children': [child.to_dict() for child in self.children]
        }
