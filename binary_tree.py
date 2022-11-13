"""
Задача:
Реализовать структуру бинарное дерево.

Сделала валидацию значений узлов в соответствии с требованиями для бинарного дерева.
Сделала собственный класс исключений.
"""


# Общий класс исключений
class KnotExeption(Exception):
    pass


# Делаем исключение для левого потомка
class LeftKnotExeption(KnotExeption):
    def __init__(self, *args):
        super().__init__(*args)
        self.text = args[0] if args else None

    def __str__(self):
        return f'Ошибка левого потомка {self.text}'


# Делаем исключение для правого потомка
class RightKnotExeption(KnotExeption):
    def __init__(self, *args):
        super().__init__(*args)
        self.text = args[0] if args else None

    def __str__(self):
        return f'Ошибка правого потомка {self.text}'


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

        # добавить левого потомка
    def insert_left(self, new_node):
        try:
            if new_node < self.root:
                # если у узла нет левого потомка
                if self.left_child is None:
                    # тогда узел просто вставляется в дерево
                    # формируется новое поддерево
                    self.left_child = BinaryTree(new_node)
                # если у узла есть левый потомок
                else:
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(new_node)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
            else:
                raise LeftKnotExeption
        except LeftKnotExeption:
            print(f'Значение больше, чем должен быть левый потомок')

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if new_node >= self.root:
                # если у узла нет правого потомка
                if self.right_child is None:
                    # тогда узел просто вставляется в дерево
                    # формируется новое поддерево
                    self.right_child = BinaryTree(new_node)
                # если у узла есть правый потомок
                else:
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(new_node)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
            else:
                raise RightKnotExeption
        except RightKnotExeption:
            print(f'Значение меньше, чем должен быть правый потомок')

# метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(1)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(74)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
print('----------------------------------')
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(73278)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(1)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
