from MyStack import MyStack

if __name__ == '__main__':
    balanced = False
    i = 0
    new_stack = MyStack([])
    open_bracket = ["(", "[", "{"]
    close_bracket = [")", "]", "}"]
    # сбалансированные последовательности скобок
    test_string = '(((([{}]))))'
    # test_string = '[([])((([[[]]])))]{()}'
    # test_string = '{{[()]}}'
    # НЕ сбалансированные последовательности скобок
    # test_string = '}{}'
    # test_string = '{{[(])]}}'
    # test_string = '[[{())}]'
    test_list = list(test_string)
    for item in test_list:
        print(f'стек: {list(new_stack)}')
        if i == 0 and item in close_bracket:
            balanced = False
            break
        if item in open_bracket:
            print(f"добавляем элемент: '{item}'")
            new_stack.push(item)
        else:
            pos = open_bracket.index(new_stack.peek())
            if close_bracket[pos] == item:
                print(f"найдена закрывающая скобка '{item}', "
                      f"удаляем соответствующую ей '{new_stack.peek()}' открывающую")
                new_stack.pop()
                balanced = True
            else:
                print(f"найдена закрывающая скобка '{item}', "
                      f"НЕ соответствующая '{new_stack.peek()}' открывающей")
                balanced = False
                break
        i += 1
    if new_stack.is_empty() and balanced:
        print(f'стек пуст: {list(new_stack)}')
        print('Сбалансированно')
    else:
        print('Несбалансированно')
