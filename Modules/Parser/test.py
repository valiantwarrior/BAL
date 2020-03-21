import bal_parser


def main() :
    expr = "=ROUND(S11*(1-U11*4)/(2*2.5),0)*2*2.5"
    bal_parser.expr_to_postfix(expr)

if __name__ == "__main__" :
    main()