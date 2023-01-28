import sys


def getType(node, scope):
    node_type = node.node_type
    if node_type == "ATOM":
        return node.type
    elif node_type == "ID":
        return scope[node.value][1]
    elif node_type == "UNARY" or node_type == "BINARY":
        return node.op_value_type


def begin(name):
    code = ".bytecode 50.0\n"
    code += f".class public {name}\n"
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
        if var_type == "FLOAT":
            func_vars[var] = (i, var_type)
            i += 2
        else:
            func_vars[var] = (i, var_type)
            i += 1
    return func_vars, i


def printStmt(statments, label_nums, scope, code):
    for stmt in statments:
        node_type = stmt.node_type

        if node_type == "ASSIGN":
            code = printAssign(stmt, scope, code)
        elif node_type == "FUNCCALL":
            code = printFuncCall(stmt, scope, code)
        elif node_type == "IF":
            code = printIf(stmt, label_nums, scope, code)
        elif node_type == "IF_ELSE":
            code = printIfElse(stmt, label_nums, scope, code)

    return code


def printDecl(declarations, scope, code):
    for decl in declarations:
        if decl.children is not None:
            var = scope[decl.value]
            var_type = var[1]
            # print(decl.children)
            expr = decl.children[0]
            code = printExpr(expr, var_type, scope,  code)
        code = storeVar(var[0], var_type, code)
    return code


def printExpr(expr, var_type, scope, code):
    if expr.node_type == "ATOM":
        if var_type == "FLOAT":
            if getType(expr, scope) == "INT":
                code += f"  ldc {expr.value}\n"
                code += "  i2d\n"
            else:
                code += f"  ldc2_w {expr.value}D\n"
        elif var_type == "INT":
            code += f"  ldc {expr.value}\n"
        elif var_type == "STRING":
            code += f"  ldc {expr.values}\n"
    elif expr.node_type == "UNARY":
        code = printUnary(expr, var_type, scope, code)
    elif expr.node_type == "BINARY":
        code = printBinary(expr, var_type, scope, code)
    elif expr.node_type == "ID":
        var_num, var_type = scope[expr.value]
        code = loadVar(var_num, var_type, code)
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

    elif expr.value == "%":
        if var_type == "INT":
            code += f"  irem\n"
        elif var_type == "FLOAT":
            code += f"  drem\n"

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


def printAssign(stmt, scope, code):
    var_name = stmt.value
    var_num, var_type = scope[var_name]

    code = printExpr(stmt.children[0], var_type, scope, code)
    code = storeVar(var_num, var_type, code)
    return code


def printIf(node, label_nums, scope, code):
    expr, stmt = node.children
    if_num = label_nums["if"]
#    if expr.value in [">", "<", ">=", "<="]:

    op_value_type = expr.op_value_type
    code = printExpr(expr.children[0], op_value_type, scope, code)
    code = printExpr(expr.children[1], op_value_type, scope, code)
    if op_value_type == "INT":
        if expr.value == ">":
            code += f"  if_icmple if_end_{if_num}\n"
        elif expr.value == ">=":
            code += f"  if_icmplt if_end_{if_num}\n"
        elif expr.value == "<":
            code += f"  if_icmpge if_end_{if_num}\n"
        elif expr.value == "<=":
            code += f"  if_icmpgt if_end_{if_num}\n"
        elif expr.value == "==":
            code += f"  if_icmpne if_end_{if_num}\n"
        elif expr.value == "!=":
            code += f"  if_icmpeq if_end_{if_num}\n"
    elif op_value_type == "FLOAT":
        code += f"  dcmpg\n"
        if expr.value == ">":
            code += f"  ifle if_end_{if_num}\n"
        elif expr.value == ">=":
            code += f"  iflt if_end_{if_num}\n"
        elif expr.value == "<":
            code += f"  ifge if_end_{if_num}\n"
        elif expr.value == "<=":
            code += f"  ifgt if_end_{if_num}\n"
        elif expr.value == "==":
            code += f"  ifne if_end_{if_num}\n"
        elif expr.value == "!=":
            code += f"  ifeq if_end_{if_num}\n"
    code = printStmt(stmt.children, label_nums, scope, code)
    code += f"if_end_{if_num}:\n"
    label_nums["if"] += 1
    return code


def printIfElse(node, label_nums, scope, code):
    expr, if_part, else_part = node.children
    if_else_num = label_nums["if_else"]
#    if expr.value in [">", "<", ">=", "<="]:

    op_value_type = expr.op_value_type
    code = printExpr(expr.children[0], op_value_type, scope, code)
    code = printExpr(expr.children[1], op_value_type, scope, code)
    if op_value_type == "INT":
        if expr.value == ">":
            code += f"  if_icmple if_else_{if_else_num}\n"
        elif expr.value == ">=":
            code += f"  if_icmplt if_else_{if_else_num}\n"
        elif expr.value == "<":
            code += f"  if_icmpge if_else_{if_else_num}\n"
        elif expr.value == "<=":
            code += f"  if_icmpgt if_else_{if_else_num}\n"
        elif expr.value == "==":
            code += f"  if_icmpeq if_else_{if_else_num}\n"
        elif expr.value == "!=":
            code += f"  if_icmpne if_else_{if_else_num}\n"

    elif op_value_type == "FLOAT":
        code += f"  dcmpg\n"
        if expr.value == ">":
            code += f"  ifle if_else_{if_else_num}\n"
        elif expr.value == ">=":
            code += f"  iflt if_else_{if_else_num}\n"
        elif expr.value == "<":
            code += f"  ifge if_else_{if_else_num}\n"
        elif expr.value == "<=":
            code += f"  ifgt if_else_{if_else_num}\n"
        elif expr.value == "==":
            code += f"  ifne if_else_{if_else_num}\n"
        elif expr.value == "!=":
            code += f"  ifeq if_else_{if_else_num}\n"

    code = printStmt(if_part.children, label_nums, scope, code)
    code += f"  goto if_else_end_{if_else_num}\n"
    code += f"if_else_{if_else_num}:\n"
    code = printStmt(else_part.children, label_nums, scope, code)
    code += f"if_else_end_{if_else_num}:\n"
    label_nums["if_else"] += 1

    return code


def printWhile():
    pass


def printFuncCall(stmt, scope, code):
    if stmt.value == "fmt.Println":
        arg = stmt.args[0]
        var_type = getType(arg, scope)
        code += "  getstatic java/lang/System/out Ljava/io/PrintStream;\n"
        code = printExpr(arg, var_type, scope, code)
        if var_type == "INT":
            code += f"  invokevirtual java/io/PrintStream/println(I)V\n"
        elif var_type == "FLOAT":
            code += f"  invokevirtual java/io/PrintStream/println(D)V\n"
    else:
        pass

    return code


def loadVar(var_num, var_type, code):
    if var_type == "INT":
        code += f"  iload {var_num}\n"
    elif var_type == "FLOAT":
        code += f"  dload {var_num}\n"
    return code


def storeVar(var_num, var_type, code):
    if var_type == "INT":
        code += f"  istore {var_num}\n"
    elif var_type == "FLOAT":
        code += f"  dstore {var_num}\n"
    return code


def codeGen(tree, filename):
    code = begin(filename)
    ast = tree.ast
    label_num = {"if": 0, "if_else": 0, "while": 0}
    if ast == None:
        sys.exit("CAN'T GENERATE CODE FROM EMPTY AST")

    for func in ast.children:
        func_vars, locals_limit = setFuncScope(func.scope)
        code = setFuncStart(func, locals_limit, code)
        body = func.children[0].children
        for block in body:
            node_type = block.node_type
            if node_type == "DECL":
                code = printDecl(block.children, func_vars, code)
            if node_type == "STMT":
                code = printStmt(block.children, label_num, func_vars, code)

        if code.endswith("  return\n"):
            code += ".end method\n"
        else:
            code += "  return\n.end method\n"

    return code
