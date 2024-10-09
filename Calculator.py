while True:

    operator = (input("Input your mathematical operation here: "))
    num1 = float((input("Input your first number here: ")))
    num2 = float((input("Input your second number here: ")))

    plus = "+"
    minus = "-"
    divide = "/"
    mult = "*"
    expo = "**"

    answer1 = num1 + num2
    answer2 = num1 - num2
    answer3 = num1 / num2
    answer4 = num1 * num2
    answer5 = num1 ** num2

    if operator == plus:
        print(num1, "+", num2, "=", answer1)

    elif operator == minus:
        print(num1, "-", num2, "=", answer2)

    elif operator == divide:
        print(num1, "/", num2, "=", answer3)

    elif operator == mult:
        print(num1, "*", num2, "=", answer4)
    
    elif operator == expo:
        print(num1, "**", num2, "=", answer5)
   