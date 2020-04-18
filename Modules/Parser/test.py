import bal_parser


def main() :
    expr = "=ROUND(BPINT*(1-0.125*4)/(2*2.5),0)*2*2.5"
    postfix = bal_parser.expr_to_postfix(expr)
   
    result = bal_parser.calculate(postfix, 105)
    print(result)


if __name__ == "__main__" :
    main()