import ply.yacc as yacc
from lexer import tokens 
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from compiler.semantic_analyzer import SemanticAnalyzer
from compiler.code_generator import CodeGenerator

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from compiler.intermediate import ASTNode  # This import will work now

def p_statement_expr(p):
    'statement : expression'
    p[0] = ASTNode('stmt', children=[p[1]])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULT expression
                  | expression DIV expression'''
    p[0] = ASTNode('binop', children=[p[1], p[3]], value=p[2])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ASTNode('num', value=p[1])

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = ASTNode('var', value=p[1])

def p_expression_assignment(p):
    'expression : IDENTIFIER EQUALS expression'
    var_node = ASTNode('var', value=p[1])
    p[0] = ASTNode('assign', children=[var_node, p[3]])

def p_error(p):
    print("Syntax error!")

parser = yacc.yacc()

# Test it
if __name__ == "__main__":
    code = "x = 5 + 3"
    result = parser.parse(code)
    print(result.to_dict())  # Optional debug print

    import json
    with open("compiler/output_ast.json", "w") as f:
        json.dump(result.to_dict(), f, indent=4)

if __name__ == "__main__":
    code = "x = 5 + 3"  # You can change this for testing
    result = parser.parse(code)
    
    print("Parsed AST:")
    print(result)

    # Semantic Analysis
    analyzer = SemanticAnalyzer()
    try:
        analyzer.analyze(result.children[0])
        print("Semantic analysis passed ✅")
    except Exception as e:
        print(f"Semantic analysis failed ❌: {e}")
        exit(1)

    # Code Generation
    generator = CodeGenerator()
    generated_code = generator.generate(result)

    print("\nGenerated Code:")
    print(generated_code)

    # 🔽 Add this block to save the generated code
    with open("output.py", "w") as f:
         f.write(generated_code)



