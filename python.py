while True:
    n1 = float(input('1? - '))
    action = input('+-*/: ')
    n2 = float(input('2? - '))

    if action == '+':
        answer = n1 + n2
        print(answer)
    elif action == '-':
        answer = n1 - n2
        print(answer)
    elif action == '*':
        answer = n1 * n2
        print(answer)
    elif action == '/' and n2 == 0:
        answer = n1 / n2
        print(answer)
