import re

class Lexer:
    def __init__(self):
        self.token_patterns = [
            (r'\"[^"]*\"|\'.*?\'', 'STRING'),  # Process STRING first
            (r'\b(def|class|return|if|else|while|for|import|from|as|pass)\b', 'KEYWORD'),  # Keywords
            (r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', 'IDENTIFIER'),  # Identifiers
            (r'\d+(\.\d+)?', 'NUMBER'),  # Numbers (including floats)
            (r'==|!=|<=|>=|\+|-|\*|/|=', 'OPERATOR'),  # Operators
            (r'[\(\)\{\}\[\]]', 'DELIMITER'),  # Delimiters
            (r'#.*', 'COMMENT'),  # Comments
            (r'\s+', None)  # Ignore whitespace
        ]

    def tokenize(self, code):
        tokens = []
        while code:
            match_found = False
            for pattern, token_type in self.token_patterns:
                match = re.match(pattern, code)
                if match:
                    match_found = True
                    if token_type:  # Ignore whitespace
                        tokens.append((match.group(), token_type))
                    code = code[len(match.group()):]  # Move forward
                    break
            if not match_found:  # If no match is found, break to avoid infinite loop
                raise ValueError(f"Unexpected character: {code[0]}")
        return tokens
