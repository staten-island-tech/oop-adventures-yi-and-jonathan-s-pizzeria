print("A math expression is something like 3+5+7 (no spaces)")
math_expression = raw_input("Enter a math expression: ")
result = eval(math_expression)
print("Result of %s is %s" % (math_expression, result))