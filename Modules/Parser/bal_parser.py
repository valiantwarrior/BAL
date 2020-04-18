import re
import sys
import decimal

op=['+','-','*','/','(',')',',','round', '=']


def tokenize(expStr):


    tok = []

    i = 0
    j = 0
    while i < len(expStr):
    
        if expStr[i] not in op:
            if(i == len(expStr)-1):
                if(i == j):
                    tok.append(expStr[i])
                else:
                    tok.append(expStr[j:i+1])
                
            i += 1
        
            continue

        else:
            if(i == j):
                tok.append(expStr[i])
            else:
                tok.append(expStr[j:i])
                tok.append(expStr[i])
            i += 1
            j = i

    
    return tok


def expr_to_postfix(expr):
    
    result = []

    expr = expr.replace(" ", "")
    expr = expr.lower()
   
    tokens = tokenize(expr)
    p = {
        "*" : 50,
        "/" : 50,
        "+" : 40,
        "-" : 40,
        "(" : 0,
        ")" : 0,
        "," : 0,
        "round" : 0,
        "=" : 0
    }
    stack = []

    for item in tokens:
        if item not in op:
            result.append(item)

        elif item == '=':
            continue;

        elif item == '(':
            stack.append(item)

        elif item =='round':
            stack.append(item)

        elif item ==')':
            while stack != [] and \
                    stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
            if stack != [] and \
                   stack[-1] == 'round':
                result.append(stack.pop())

        elif item == ',':
            while stack != [] and \
                    p[stack[-1]] > p[item]:
                result.append(stack.pop())
        

        else:
            while stack != [] and \
                    p[stack[-1]] >= p[item]:
                result.append(stack.pop())
            stack.append(item)


    while stack:
        result.append(stack.pop())
    
    for i in range(0, len(result)) :
        result[i] = convert_str2num(result[i])

    print(result)

    return result


def inputs(postfix) :
    
    ret = []
    p = re.compile('[a-zA-Z]+[0-9]*')
    for c in postfix :
        if p.match(c) and c not in op :
            ret.append(c)

    return ret


def convert_str2num(str) :
    int_p = re.compile('[1-9]+[0-9]*')
    float_p = re.compile('[1-9]*[0-9]+\.[0-9]*')

    if float_p.match(str) :
        return float(str)
    
    if int_p.match(str) :
        return int(str)

    return str
    

def operation(operand1, operand2, operator) :
    
    if operator == '+' :
        return operand1 + operand2
    elif operator == '-' :
        return operand1 - operand2
    elif operator == '*' :
        return operand1 * operand2
    elif operator == '/' :
        return operand1 / operand2
    elif operator == 'round' :
        return int(operand1) + 1 if (operand1 - int(operand1)) >= 0.5 else int(operand1)
    else :
        pass


def calculate(postfix, inputs) :

    index = postfix.index('bpint')
    postfix[index] = inputs
    stack = []

    for i in range(0, len(postfix)) :
        if postfix[i] in op :
            param2 = stack.pop()
            param1 = stack.pop()
            inner = operation(param1, param2, postfix[i])
            stack.append(inner)
        else :
            stack.append(postfix[i])

    result = stack.pop()

    return result

