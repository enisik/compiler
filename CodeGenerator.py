import sys


def bti(bool):
    if bool == "true":
        return 1
    elif bool == "false":
        return 0
    else:
        sys.exit("Something went wrong!")


def typeToJVM(type):
    if type == "INT":
        return "I"
    elif type == "FLOAT":
        return "D"
    elif type == "BOOL":
        return "Z"
    elif type == "STRING":
        return "Ljava/lang/String;"
    elif type == None:
        return "V"


def getType(node, scope, global_scope):
    node_type = node.node_type
    if node_type == "ATOM":
        return node.type
    elif node_type == "ID":
        return scope[node.value][1]
    elif node_type == "UNARY" or node_type == "BINARY":
        return node.op_value_type
    elif node_type == "FUNCCALL":
        return global_scope[node.value][1]


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


def setFuncStart(func, func_args, len_vars, func_return_type, code):

    if func.value == "main":
        code += ".method public static main([Ljava/lang/String;)V\n"
        code += "  .limit stack 100\n"
        code += f"  .limit locals {len_vars}\n"
    else:
        code += f".method public static {func.value}("
        if func_args is not None:
            for arg in func_args:
                code += typeToJVM(arg[1])

        code += f"){typeToJVM(func_return_type)}\n"
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
    if i == 0:
        i += 1
    return func_vars, i


def printStmt(statments, label_nums, scope, code, global_scope):
    for stmt in statments:
        node_type = stmt.node_type

        if node_type == "ASSIGN":
            code = printAssign(stmt, label_nums, scope, code, global_scope)
        elif node_type == "FUNCCALL":
            code = printFuncCall(stmt, label_nums, scope, code, global_scope)
        elif node_type == "IF":
            code = printIf(stmt, label_nums,
                           scope, code, global_scope)
        elif node_type == "IF_ELSE":
            code = printIfElse(stmt, label_nums, scope, code, global_scope)
        elif node_type == "FOR":
            code = printWhile(stmt, label_nums, scope, code, global_scope)
        else:
            code = printReturn(stmt, label_nums, scope, code, global_scope)

    return code


def printReturn(stmt, label_nums, scope, code, global_scope):
    return_expr = stmt.children[0]
    return_type = global_scope[label_nums["func_name"]][1]
    if return_expr is None:
        expr_type = None
    else:
        expr_type = getType(return_expr, scope, global_scope)
        code = printExpr(return_expr, expr_type, label_nums,
                         scope, code, global_scope)
    if expr_type == "INT" or expr_type == "BOOL":
        if return_type == "FLOAT":
            code += f"  i2d\n  dreturn\n"
        else:
            code += f"  ireturn\n"
    elif expr_type == "FLOAT":
        code += f"  dreturn\n"
    elif expr_type == "STRING":
        code += f"  areturn\n"
    elif expr_type is None:
        code += f"  return\n"
    return code


def printDecl(declarations, label_nums, scope, code, global_scope):
    for decl in declarations:
        if decl.children is not None:
            var = scope[decl.value]
            var_type = var[1]
            # print(decl.children)
            expr = decl.children[0]
            op_value_type = getType(expr, scope, global_scope)
            code = printExpr(expr, op_value_type, label_nums,
                             scope, code, global_scope)

        code = storeVar(var[0], var_type, op_value_type, code)
    return code


def printExpr(expr, var_type, label_nums, scope, code, global_scope):
    if expr.node_type == "ATOM":
        if var_type == "FLOAT":
            if getType(expr, scope, global_scope) == "INT":
                code += f"  ldc {expr.value}\n"
                code += "  i2d\n"
            else:
                code += f"  ldc2_w {expr.value}D\n"
        elif var_type == "INT":
            code += f"  ldc {expr.value}\n"
        elif var_type == "STRING":
            code += f"  ldc {expr.value}\n"
        elif var_type == "BOOL":
            code += f"  ldc {bti(expr.value)}\n"
    elif expr.node_type == "UNARY":
        code = printUnary(expr, var_type, label_nums,
                          scope, code, global_scope)
    elif expr.node_type == "BINARY":
        code = printBinary(expr, var_type, label_nums,
                           scope, code, global_scope)
    elif expr.node_type == "ID":
        var_num, var_type = scope[expr.value]
        code = loadVar(var_num, var_type, code)
    elif expr.node_type == "FUNCCALL":
        code = printFuncCall(expr, label_nums, scope, code, global_scope)
    return code


def printBinary(expr, var_type, label_nums, scope, code, global_scope):
    op_value_type = expr.op_value_type

    comp_num = label_nums["comparison"]
    if expr.value in ["<", "<=", ">", ">=", "==", "!="]:
        label_nums["comparison"] += 1
    code = printExpr(expr.children[0], op_value_type,
                     label_nums, scope, code, global_scope)
    code = printExpr(expr.children[1], op_value_type,
                     label_nums, scope, code, global_scope)
    operand_type = getType(expr.children[0], scope, global_scope)
    if var_type == "FLOAT" and operand_type == "INT":
        var_type = "INT"
    if expr.value == "+":
        if var_type == "INT":
            code += f"  iadd\n"
        elif var_type == "FLOAT":
            code += f"  dadd\n"
        return code

    elif expr.value == "-":
        if var_type == "INT":
            code += f"  isub\n"
        elif var_type == "FLOAT":
            code += f"  dsub\n"
        return code

    elif expr.value == "*":
        if var_type == "INT":
            code += f"  imul\n"
        elif var_type == "FLOAT":
            code += f"  dmul\n"
        return code

    elif expr.value == "/":
        if var_type == "INT":
            code += f"  idiv\n"
        elif var_type == "FLOAT":
            code += f"  ddiv\n"
        return code

    elif expr.value == "%":
        if var_type == "INT":
            code += f"  irem\n"
        elif var_type == "FLOAT":
            code += f"  drem\n"
        return code

    elif expr.value == "&&":
        code += f"  iand\n"
        return code

    elif expr.value == "||":
        code += f"  ior\n"
        return code

    elif expr.value == ">":
        if op_value_type == "INT":
            code += f"  if_icmple comp_{comp_num}_false\n"
        else:
            code += f"  dcmpg\n"
            code += f"  ifle comp_{comp_num}_false\n"

    elif expr.value == ">=":
        if op_value_type == "INT":
            code += f"  if_icmplt comp_{comp_num}_false\n"
        else:
            code += f"  dcmpg\n"
            code += f"  iflt comp_{comp_num}_false\n"

    elif expr.value == "<":
        if op_value_type == "INT":
            code += f"  if_icmpge comp_{comp_num}_false\n"
        else:
            code += f"  dcmpg\n"
            code += f"  ifge comp_{comp_num}_false\n"

    elif expr.value == "<=":
        if op_value_type == "INT":
            code += f"  if_icmpgt comp_{comp_num}_false\n"
        else:
            code += f"  dcmpg\n"
            code += f"  ifgt comp_{comp_num}_false\n"

    elif expr.value == "==":
        if op_value_type == "STRING":
            code += f"  invokevirtual java/lang/String.equals(Ljava/lang/Object;)Z\n"
            return code
        elif op_value_type == "INT" or op_value_type == "BOOL":
            code += f"  ifne comp_{comp_num}_false\n"
        elif op_value_type == "FLOAT":
            code += f"  dcmpg\n"
            code += f"  ifne comp_{comp_num}_false\n"

    elif expr.value == "!=":
        if op_value_type == "STRING":
            code += f"  invokevirtual java/lang/String.equals(Ljava/lang/Object;)Z\n"
            code += f"  iconst_1\n  ixor\n"
            return code
        elif op_value_type == "INT" or op_value_type == "BOOL":
            code += f"  ifeq comp_{comp_num}_false\n"
        elif op_value_type == "FLOAT":
            code += f"  dcmpg\n"
            code += f"  ifeq comp_{comp_num}_false\n"

    code += f"  iconst_1\n  goto comp_{comp_num}_end\n"
    code += f"comp_{comp_num}_false:\n"
    code += f"  iconst_0\n"
    code += f"comp_{comp_num}_end:\n"

    return code


def printUnary(expr, var_type, label_nums, scope, code, global_scope):
    code = printExpr(expr.children[0], var_type,
                     label_nums, scope, code, global_scope)
    if expr.value == "-":
        if var_type == "INT":
            code += f"  ineg\n"
        elif var_type == "FLOAT":
            code += f"  dneg\n"
    elif expr.value == "+":
        return code
    elif expr.value == "!":
        code += f"  iconst_1\n"
        code += f"  ixor\n"

    return code


def printAssign(stmt, label_nums, scope, code, global_scope):
    var_name = stmt.value
    var_num, var_type = scope[var_name]

    code = printExpr(stmt.children[0], var_type,
                     label_nums, scope, code, global_scope)
    op_value_type = getType(stmt.children[0], scope, global_scope)
    code = storeVar(var_num, var_type, op_value_type, code)
    return code


def printIf(node, label_nums, scope, code, global_scope):
    expr, stmt = node.children
    if_num = label_nums["if"]
    label_nums["if"] += 1
#    if expr.value in [">", "<", ">=", "<="]:

    expr_type = expr.node_type
    if expr_type == "ID" or expr_type == "ATOM":
        code = printExpr(expr, "BOOL", label_nums, scope, code, global_scope)
        code += f"  ifeq if_end_{if_num}\n"
    else:
        op_value_type = expr.op_value_type
        code = printExpr(
            expr.children[0], op_value_type, label_nums, scope, code, global_scope)
        code = printExpr(
            expr.children[1], op_value_type, label_nums, scope, code, global_scope)
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
        elif op_value_type == "BOOL":
            code = printExpr(expr, "BOOL", label_nums,
                             scope, code, global_scope)
            code += f"  ifeq if_end_{if_num}\n"

    if stmt is not None:
        code = printStmt(stmt.children, label_nums, scope, code, global_scope)
    code += f"if_end_{if_num}:\n"
    return code


def printIfElse(node, label_nums, scope, code, global_scope):
    expr, if_part, else_part = node.children
    if_else_num = label_nums["if_else"]
    label_nums["if_else"] += 1

    expr_type = expr.node_type
    if expr_type == "ID" or expr_type == "ATOM":
        code = printExpr(expr, "BOOL", label_nums, scope, code, global_scope)
        code += f"  ifeq if_else_{if_else_num}\n"
    else:
        op_value_type = expr.op_value_type
        code = printExpr(expr.children[0],
                         op_value_type, label_nums, scope, code, global_scope)
        code = printExpr(expr.children[1],
                         op_value_type, label_nums, scope, code, global_scope)
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

        elif op_value_type == "BOOL":
            code = printExpr(expr, "BOOL", label_nums,
                             scope, code, global_scope)
            code += f"  ifeq if_else_{if_else_num}\n"

    if if_part is not None:
        code = printStmt(if_part.children, label_nums,
                         scope, code, global_scope)
    code += f"  goto if_else_end_{if_else_num}\n"
    code += f"if_else_{if_else_num}:\n"
    if else_part is not None:
        code = printStmt(else_part.children, label_nums,
                         scope, code, global_scope)
    code += f"if_else_end_{if_else_num}:\n"

    return code


def printWhile(node, label_nums, scope, code, global_scope):
    expr, stmt = node.children
    while_num = label_nums["while"]
    label_nums["while"] += 1

    code += f"  goto while_{while_num}_check\n"

    code += f"while_{while_num}_body:\n"
    if stmt is not None:
        code = printStmt(stmt.children, label_nums, scope, code, global_scope)

    code += f"while_{while_num}_check:\n"
    expr_type = expr.node_type
    if expr_type == "ID" or expr_type == "ATOM":
        code = printExpr(expr, "BOOL", label_nums, scope, code, global_scope)
        code += f"  ifne while_{while_num}_body\n"
        return code
    op_value_type = expr.op_value_type
    if op_value_type == "INT":
        code = printExpr(expr.children[0], op_value_type,
                         label_nums, scope, code, global_scope)
        code = printExpr(expr.children[1], op_value_type,
                         label_nums, scope, code, global_scope)
        if expr.value == ">":
            code += f"  if_icmpgt while_{while_num}_body\n"
        elif expr.value == ">=":
            code += f"  if_icmpge while_{while_num}_body\n"
        elif expr.value == "<":
            code += f"  if_icmplt while_{while_num}_body\n"
        elif expr.value == "<=":
            code += f"  if_icmple while_{while_num}_body\n"
        elif expr.value == "==":
            code += f"  if_icmpeq while_{while_num}_body\n"
        elif expr.value == "!=":
            code += f"  if_icmpne while_{while_num}_body\n"
    elif op_value_type == "FLOAT":
        code = printExpr(expr.children[0], op_value_type,
                         label_nums, scope, code, global_scope)
        code = printExpr(expr.children[1], op_value_type,
                         label_nums, scope, code, global_scope)
        code += f"  dcmpg\n"
        if expr.value == ">":
            code += f"  ifgt while_{while_num}_body\n"
        elif expr.value == ">=":
            code += f"  ifge while_{while_num}_body\n"
        elif expr.value == "<":
            code += f"  iflt while_{while_num}_body\n"
        elif expr.value == "<=":
            code += f"  ifle while_{while_num}_body\n"
        elif expr.value == "==":
            code += f"  ifeq while_{while_num}_body\n"
        elif expr.value == "!=":
            code += f"  ifne while_{while_num}_body\n"
    elif op_value_type == "BOOL":
        code = printExpr(expr, "BOOL", label_nums, scope, code, global_scope)
        code += f"  ifne while_{while_num}_body\n"
    return code


def printFuncCall(stmt, label_nums, scope, code, global_scope):
    if stmt.value == "fmt.Println":
        if stmt.args is None:
            return code
        arg = stmt.args[0]
        var_type = getType(arg, scope, global_scope)
        code += "  getstatic java/lang/System/out Ljava/io/PrintStream;\n"
        code = printExpr(arg, var_type, label_nums, scope, code, global_scope)
        if var_type == "INT":
            code += f"  invokevirtual java/io/PrintStream/println(I)V\n"
        elif var_type == "FLOAT":
            code += f"  invokevirtual java/io/PrintStream/println(D)V\n"
        elif var_type == "STRING":
            code += f"  invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V\n"
        elif var_type == "BOOL":
            code += f"  invokevirtual java/io/PrintStream/println(Z)V\n"
    else:
        func_args, return_type = global_scope[stmt.value]
        i = 0
        if stmt.args is not None:
            for arg in stmt.args:
                var_type = getType(arg, scope, global_scope)
                code = printExpr(arg, var_type, label_nums,
                                 scope, code, global_scope)
                func_arg_type = func_args[i][1]
                if func_arg_type == "FLOAT" and var_type == "INT":
                    code += f"  i2d\n"
                i += 1

        code += f"  invokestatic {label_nums['class_name']}/{stmt.value}("
        if func_args is not None:
            for arg in func_args:
                code += typeToJVM(arg[1])
        code += f"){typeToJVM(return_type)}\n"

    return code


def loadVar(var_num, var_type, code):
    if var_type == "INT" or var_type == "BOOL":
        code += f"  iload {var_num}\n"
    elif var_type == "FLOAT":
        code += f"  dload {var_num}\n"
    elif var_type == "STRING":
        code += f"  aload {var_num}\n"
    return code


def storeVar(var_num, var_type, expr_value, code):
    if var_type == "INT" or var_type == "BOOL":
        code += f"  istore {var_num}\n"
    elif var_type == "FLOAT":
        if expr_value == "INT":
            code += "  i2d\n"
        code += f"  dstore {var_num}\n"
    elif var_type == "STRING":
        code += f"  astore {var_num}\n"
    return code


def codeGen(tree, filename):
    code = begin(filename)
    ast = tree.ast
    global_scope = tree.global_scope
    label_nums = {"if": 0, "if_else": 0, "while": 0,
                  "comparison": 0, "class_name": filename}
    if ast == None:
        sys.exit("CAN'T GENERATE CODE FROM EMPTY AST")

    for func in ast.children:
        label_nums["func_name"] = func.value
        func_vars, locals_limit = setFuncScope(func.scope)
        func_args, func_return_type = global_scope[func.value]
        code = setFuncStart(func, func_args, locals_limit,
                            func_return_type, code)
        body = func.children[0].children
        for block in body:
            node_type = block.node_type
            if node_type == "DECL":
                code = printDecl(block.children, label_nums,
                                 func_vars, code, global_scope)
            if node_type == "STMT":
                code = printStmt(block.children, label_nums,
                                 func_vars, code, global_scope)

        if code.endswith("return\n"):
            code += ".end method\n\n"
        else:
            code += "  return\n.end method\n\n"

    return code
