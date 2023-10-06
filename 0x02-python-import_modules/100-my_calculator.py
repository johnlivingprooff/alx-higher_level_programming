#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, op, b = sys.argv[1], sys.argv[2], sys.argv[3]
    a, b = int(a), int(b)
    result = None

    match op:
        case "+":
            result = add(a, b)
        case "*":
            result = mul(a, b)
        case "-":
            result = sub(a, b)
        case "/":
            result = div(a, b)
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

    print("{} {} {} = {}".format(a, op, b, result))
