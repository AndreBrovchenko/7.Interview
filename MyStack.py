class MyStack:

    def __init__(self, input_list):
        """ инициализация стека """
        self.list = input_list

    def __iter__(self):
        """ метод позволяет при передаче объекта функции iter возвращать самого себя """
        self.cursor = 0
        return self

    def __next__(self):
        """ извлекаем следующий элемент """
        if self.cursor > len(self.list) - 1:
            raise StopIteration
        list_item = self.list[self.cursor]
        self.cursor += 1
        return list_item

    def is_empty(self):
        """ провека стека на пустоту """
        if len(self.list) > 0:
            return False
        else:
            return True

    def push(self, item):
        """ добавляет новый элемент на вершину стека """
        self.list.append(item)

    def pop(self):
        """ удаляет элемент из вершины стека """
        if len(self.list) > 0:
            self.list.pop()
        else:
            print('удалять нечего, стек пуст')

    def peek(self):
        """ возвращает верхний элемент стека, но не удаляет его """
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return print('стек пуст')

    def size(self):
        """ возвращает количество элементов в стеке """
        return len(self.list)

