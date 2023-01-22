import sys


def begin():
    code = ".bytecode 50.0\n"
    code += ".class public Goprog\n"
    code += ".super java/lang/Object\n"
    code += ".method public <init>()V\n"
    code += "  .limit stack 1\n"
    code += "  .limit locals 1\n"
    code += "  aload_0\n"
    code += "  invokespecial java/lang/Object/<init>()V\n"
    code += "  return\n"
    code += ".end method\n\n"
    return code


def setFuncStart(func, len_vars, code):

    if func.value == "main":
        code += ".method public static main([Ljava/lang/String;)V\n"
        code += "  .limit stack 100\n"
        code += f"  .limit locals {len_vars}\n"
    else:
        code += f".method public static {func.value}()V\n"
        code += "  .limit stack 100\n"
        code += f"  .limit locals {len_vars}\n"
    return code


def setFuncScope(func_vars):
    i = 0
    for var in func_vars.keys():
        var_type = func_vars[var]
        func_vars[var] = (i, var_type)
        i += 1
    print(func_vars)
    return func_vars


def setFuncVars(declarations, code, scope):
    for decl in declarations:
        print(decl)
        if decl.children is not None:
            code = printDecl(
                decl.children, scope[decl.value], scope, code)

    return code


def printStmt(statments, code):
    for stmt in statments:
        if stmt.children is not None:
            # code =
            pass
    return code


def printDecl(declarations, scope, code):
    for decl in declarations:
        print(decl)
        if decl.children is not None:
            var = scope[decl.value]
            var_type = var[1]
            for expr in decl.children:
                code = printExpr(expr, var_type, scope,  code)
        code = storeVar(var, code)
    return code


def printExpr(expr, var_type, scope, code):
    if expr.node_type == "ATOM":
        if var_type == "FLOAT":
            code += f"  ldc_w {expr.value}\n"
        elif var_type == "INT":
            code += f"  ldc {expr.value}\n"
        elif var_type == "STRING":
            code += f"  ldc {expr.values}\n"
    elif expr.node_type == "UNARY":
        code = printUnary(expr, var_type, scope, code)
    elif expr.node_type == "BINARY":
        code = printBinary(expr, var_type, scope, code)
    elif expr.node_type == "ID":
        code = loadVar(expr.value, scope, code)
    return code


def printBinary(expr, var_type, scope, code):
    code = printExpr(expr.children[0], var_type, scope, code)
    code = printExpr(expr.children[1], var_type, scope, code)

    if expr.value == "+":
        if var_type == "INT":
            code += f"  iadd\n"
        elif var_type == "FLOAT":
            code += f"  dadd\n"

    elif expr.value == "-":
        if var_type == "INT":
            code += f"  isub\n"
        elif var_type == "FLOAT":
            code += f"  dsub\n"

    elif expr.value == "*":
        if var_type == "INT":
            code += f"  imul\n"
        elif var_type == "FLOAT":
            code += f"  dmul\n"

    elif expr.value == "/":
        if var_type == "INT":
            code += f"  idiv\n"
        elif var_type == "FLOAT":
            code += f"  ddiv\n"

    return code


def printUnary(expr, var_type, scope, code):
    code = printExpr(expr.children[0], var_type, scope, code)

    if expr.value == "-":
        if var_type == "INT":
            code += f"  ineg\n"
        elif var_type == "FLOAT":
            code += f"  dneg\n"
    elif expr.value == "+":
        return code

    return code


def printFuncCall():
    pass


def loadVar(var, scope, code):
    var_num, var_type = scope[var]
    if var_type == "INT":
        code += f"  iload {var_num}\n"
    elif var_type == "FLOAT":
        code += f"  dload {var_num}\n"
    return code


def storeVar(var, code):
    var_type = var[1]
    if var_type == "INT":
        code += f"  istore {var[0]}\n"
    elif var_type == "FLOAT":
        code += f"  dstore {var[0]}\n"
    return code


def codeGen(tree):
    code = begin()
    ast = tree.ast
    if ast == None:
        sys.exit("CAN'T GENERATE CODE FROM EMPTY AST")

    for func in ast.children:
        func_vars = setFuncScope(func.scope)
        code = setFuncStart(func, len(func_vars), code)
        body = func.children[0].children
        for block in body:
            node_type = block.node_type
            if node_type == "DECL":
                code = printDecl(block.children,  func_vars, code)
            if node_type == "STMT":
                code
                #check_stmts(block.children, func_scope, func_return, True)
        code += ".end method\n"
    return code
