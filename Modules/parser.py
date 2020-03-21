import re
import sys


op=['+','-','*','/','(',')',',','round', '=']
#문자열 토큰화
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
    print(result)
    return result



